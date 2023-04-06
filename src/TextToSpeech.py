import gtts
from playsound import playsound
from translate import Translator
import PostScraper

posttext = PostScraper.scrape()

tts_en = gtts.gTTS(posttext)
tts_en.save("./media/english.mp3")
playsound("./media/english.mp3")

translator= Translator(to_lang="Spanish")
translation = translator.translate(posttext)

tts_sp = gtts.gTTS(translation, lang="es")
tts_sp.save("./media/spanish.mp3")
playsound("./media/spanish.mp3")