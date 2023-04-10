import VideoGen
import PostContent
import Writestats

VideoGen.Generate()
Writestats.write()
PostContent.upload_to_tiktok("./media/final_english.mp4", "test", ["test1", "test2", "test3"])