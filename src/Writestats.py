import datetime
import dotenv
import os
import requests

def write():
    dotenv.load_dotenv()
    APY_API = os.environ.get("APY_API")

    payload = {'platforms': ['tiktok']}
    headers = {'Content-Type': 'application/json', 
            'Authorization': 'Bearer API_KEY'}

    r = requests.post('https://app.ayrshare.com/analytics/social', 
        json=payload, 
        headers=headers)
        
    print(r.json())
    
    f = open("demofile2.txt", "a")
    f.write("\n")
    f.write("Date: " + datetime.datetime.now())
    f.write("\n")
    f.write("Post Title:")
    f.write("\n")
    f.write("Post Share ID: " + share_id)
    f.write("\n")
    f.write("Current Follower Count:")
    f.write("\n")
    f.write("Current Like Total:")
    f.write("\n")
    f.write("Total # of Videos:")
    f.close()
