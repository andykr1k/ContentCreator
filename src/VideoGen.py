from translate import Translator
import PostScraper
import TextToSpeech
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from moviepy.editor import *

posttext_english = PostScraper.scrape()

translator = Translator(to_lang="Spanish")
# translation = translator.translate(posttext_english)

TextToSpeech.Generate(posttext_english)

split_en = posttext_english.split()
# split_es = translation.split()

    
clip = VideoFileClip("./media/video.mp4") 
clip = clip.subclip(0, 25) 
clip = clip.volumex(1) 
txt_clip = TextClip(posttext_english, fontsize = 75, color = 'black') 
txt_clip = txt_clip.set_pos('center').set_duration(25) 
video = CompositeVideoClip([clip, txt_clip]) 
    
video.ipython_display(width = 1080, height=1920) 

video.write_videofile('./media/final_english.mp4',fps=30,codec='mpeg4')
