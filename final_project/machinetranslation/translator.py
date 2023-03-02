import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Return translated text ."""
    #write the code here
    if english_text is None:
        return None
    else:
        text_to_translate = english_text
        translation = language_translator.translate(
        text=text_to_translate,
        model_id='en-fr').get_result()
        dump_result = json.dumps(translation, indent=2, ensure_ascii=False)
        loaded_r = json.loads(dump_result)
        result = loaded_r['translations'][0]['translation']
        return result

def english_to_somali(text):
    """Return translated text ."""
    #write the code here
    if text is None:
        return None
    else:
        text_to_translate = text
        translation = language_translator.translate(
        text=text_to_translate,
        model_id='en-fr').get_result()
        dump_result = json.dumps(translation, indent=2, ensure_ascii=False)
        loaded_r = json.loads(dump_result)
        result = loaded_r['translations'][0]['translation']
        print(result)
        return result    


def french_to_english(french_text):
    """Return translated text ."""
    #write the code here
    if french_text is None:
        return None
    else:
        text_to_translate = french_text
        translation = language_translator.translate(
        text=text_to_translate,
        model_id='fr-en').get_result()
        dump_result = json.dumps(translation, indent=2, ensure_ascii=False)
        loaded_r = json.loads(dump_result)
        result = loaded_r['translations'][0]['translation']
        return result

english_to_somali('hello, how are you')
