from translate import Translator
import PostScraper
import TextToSpeech
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
from moviepy.editor import *

def Generate():
    posttext_english = PostScraper.scrape()

    # translator = Translator(to_lang="Spanish")
    # translation = translator.translate(posttext_english)

    TextToSpeech.Generate(posttext_english)

    split_en = posttext_english.split()
    # split_es = translation.split()
        
    clip = VideoFileClip("./media/video.mp4").resize( (1080,1920) )
    title = ImageClip("./media/reddit.png").set_start(0).set_duration(3).set_pos(("center","center")).resize(height=50)
    clip = CompositeVideoClip([clip, title]).resize( (1080,1920) )
    audioclip = AudioFileClip("./media/english.mp3")
    clip = clip.set_audio(audioclip)
    txt_clip = TextClip(split_en[0], fontsize = 5, color = 'white').set_start(3).set_duration(3).set_pos(("center","center")).resize(height=50)
    # im_width, im_height = txt_clip.size
    # color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)), color=(0, 255, 255)).set_start(3).set_duration(3)
    # color_clip = color_clip.set_opacity(.6)
    # clip_to_overlay = CompositeVideoClip([color_clip, txt_clip]).resize( (1080,1920) )
    # clip_to_overlay = clip_to_overlay.set_position('center')
    # video = CompositeVideoClip([clip, clip_to_overlay]).resize( (1080,1920) )
    video = CompositeVideoClip([clip, txt_clip]).resize( (1080,1920) )
    video.write_videofile('./media/final_english.mp4',fps=60,codec='libx264')

Generate()