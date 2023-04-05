import tiktok_api
import dotenv
import os

def upload_to_tiktok(video_url):
    dotenv.load_dotenv()

    TT_USERNAME = os.environ.get("TT_USERNAME")
    TT_PASSWORD = os.environ.get("TT_PASSWORD")

    api = tiktok_api.TikTokApi(username=TT_USERNAME, password=TT_PASSWORD)
    api.upload(video_url)