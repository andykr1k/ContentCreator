'''
Input(vid_path) 

All query parameters are retrieved from .env file

1-Send POST request to https://open-api.tiktok.com/oauth/access_token/
Include: client_key, client_secret, code, grant_type

2- Handle response: 1? 0?

    If 1: Move on
    If 0: handle error


Now that we're in:
We have the open_id and access_token. Pass them into a new POST request for the video to https://open-api.tiktok.com/share/video/upload/

Include Body: Video_path

Did it go through?

return share_id (video identifier) to be used for ML and Analytics

'''
import dotenv
import os
import requests

def upload_to_tiktok(vid_path):
    dotenv.load_dotenv()

    CLIENT_KEY = os.environ.get("CLIENT_KEY")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CODE = os.environ.get("CODE")
    GRANT_TYPE = os.environ.get("GRANT_TYPE")


    Auth_URL = "https://open-api.tiktok.com/oauth/access_token/"
    Auth_Data =  {

    'client_key' : CLIENT_KEY,
    'client_secret' : CLIENT_SECRET,
    'code' : CODE,
    'grant_type' : GRANT_TYPE

    }

    auth_response = requests.post(Auth_URL, data = Auth_Data)
    

    if(auth_response.status_code != 200): #if unsuccessful for any reason
        print(auth_response)
        raise Exception("Authorization Error")
    

#Successful authorization - posting video
    
    Upload_URL = "https://open-api.tiktok.com/share/video/upload/"

    Upload_Data = {

        'open_id'   :   auth_response.open_id,
        'access_token' :    auth_response.access_token,
        'body'  :   {
        
        'video' :   vid_path
        }


    }
    upload_response = requests.post(Upload_URL, data = Upload_Data)

    
    if(upload_response.status_code != 200): #if unsuccessful for any reason
        print(upload_response)
        raise Exception("Upload Error")

    return upload_response.share_id


    

