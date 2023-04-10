import gtts
from playsound import playsound
# from translate import Translator

def Generate(english):

    tts_en = gtts.gTTS(english)
    tts_en.save("./media/english.mp3")
    # playsound("./media/english.mp3")

    # translator = Translator(to_lang="Spanish")
    # spanish = translator.translate(english)

    # tts_sp = gtts.gTTS(spanish, lang="es")
    # tts_sp.save("./media/spanish.mp3")
    # playsound("./media/spanish.mp3")