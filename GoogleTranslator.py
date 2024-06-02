from google.cloud import translate_v2 as translate
from translate import Translator

class GoogleTranslator:

    def __init__(self, translator_client='generic',target_language='en'):
        self.translator_client = translator_client
        self.client=translate.Client(target_language=target_language) if translator_client=='google' else Translator(to_lang=target_language)

    def translate_text(self,text:str) -> dict | str:
        
        """
        Translates text into the target language.
        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """
        if self.translator_client=='generic':
             return self.client.translate(text)
        
        if isinstance(text, bytes):
            text = text.decode("utf-8")

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = self.client.translate(text)

        print("Text: {}".format(result["input"]))
        print("Translation: {}".format(result["translatedText"]))
        print("Detected source language: {}".format(result["detectedSourceLanguage"]))

        return result

    
        
    
gt = GoogleTranslator()
x= gt.translate_text("碗是在桌子上")
print(x)