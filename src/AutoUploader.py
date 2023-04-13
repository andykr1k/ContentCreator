import dotenv
import os
import requests

def upload_to_tiktok(vid_path):
    dotenv.load_dotenv()
    APY_API = os.environ.get("APY_API")

    # CLIENT_KEY = os.environ.get("TT_CLIENT_KEY")
    # CLIENT_SECRET = os.environ.get("TT_CLIENT_SECRET")
    # CODE = os.environ.get("CODE")
    # GRANT_TYPE = os.environ.get("GRANT_TYPE")


    # Auth_URL = "https://open-api.tiktok.com/oauth/access_token/"
    # Auth_Data =  {
    #     'client_key' : CLIENT_KEY,
    #     'client_secret' : CLIENT_SECRET,
    #     'code' : CODE,
    #     'grant_type' : GRANT_TYPE
    # }

    # try:
    #     auth_response = requests.post(Auth_URL, data = Auth_Data)
    #     auth_response.raise_for_status()
    # except requests.exceptions.RequestException as e:
    #     raise SystemExit(e)
    
    # Upload_URL = "https://open-api.tiktok.com/share/video/upload/"

    # Upload_Data = {
    #     'open_id'   :   auth_response.open_id,
    #     'access_token' :    auth_response.access_token,
    #     'body'  :   {
    #                 'video' :   vid_path
    #                 }
    # }

    # try:
    #     upload_response = requests.post(Upload_URL, data = Upload_Data)
    #     upload_response.raise_for_status()
    # except requests.exceptions.RequestException as e:
    #     raise SystemExit(e)

    # return upload_response.share_id


    payload = {'post': 'Today is a great day!', 
            'platforms': ['tiktok'],
            'mediaUrls': [vid_path]}
    headers = {'Content-Type': 'application/json', 
            'Authorization': 'Bearer + {APY_API}'}

    r = requests.post('https://app.ayrshare.com/api/post', 
        json=payload, 
        headers=headers
        )
    
    print(r.json())


    

