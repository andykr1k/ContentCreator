import dotenv
import os
import lib.TikTokUploder.uploader as up

def upload_to_tiktok(video_url, title, tags):
    dotenv.load_dotenv()

    SID = os.environ.get("SESSION_ID")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    OPEN_ID = os.environ.get("OPEN_ID")
    # session_id = SID
    # file = video_url
    # title = title
    # tags = tags

    # up.uploadVideo(session_id, file, title, tags)
    command = "curl --location --request POST \'https://open-api.tiktok.com/share/video/upload/?access_token=<" + ACCESS_TOKEN + ">&open_id=<" + OPEN_ID +">\' --form \'video=@\"/Users/tiktok/Downloads/video.mp4\"\'"
    print(command)


