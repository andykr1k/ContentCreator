import VideoGen
import PostContent
import Writestats

VideoGen.Generate()
Writestats.write()
PostContent.upload_to_tiktok("./media/final.mp4")