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
    a = []
    i = 0
    d = 1

    clip = VideoFileClip("./media/video2.mp4")
    a.append(clip)

    title = ImageClip("./media/reddit.png").set_start(i).set_duration(d).set_pos(("center","center")).resize(height=100)
    a.append(title)
    i = i + d
    d = d/3

    for word in split_en:
        txt_clip = TextClip(word, fontsize = 100, color = 'white').set_start(i).set_duration(d).set_pos(("center","center"))
        a.append(txt_clip)
        i = i + d

    clip = CompositeVideoClip(a)

    audioclip = AudioFileClip("./media/english.mp3")
    new_audioclip = CompositeAudioClip([audioclip])
    final = clip.set_audio(new_audioclip)
    final = clip.subclip(0, audioclip.duration)

    final.write_videofile('./media/final_english.mp4',fps=60,codec='libx264')
