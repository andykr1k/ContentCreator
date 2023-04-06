from translate import Translator
import PostScraper

posttext_english = PostScraper.scrape()

translator= Translator(to_lang="Spanish")
translation = translator.translate(posttext_english)
