from lingua import Language, LanguageDetectorBuilder

from .DictDetector import Detector as DictDetector
import unicodedata
import fasttext
import emoji
import re
import os 

fasttext.FastText.eprint = lambda x: None

class Detector:
    def __init__(self, reliable_min:int = 0.35):
        self.lingua_detector = LanguageDetectorBuilder.from_all_spoken_languages().with_preloaded_language_models().with_low_accuracy_mode().build()

        self.fasttext_models = [
            fasttext.load_model(os.path.dirname(os.path.realpath(__file__))+"/models/lid.176.ftz"), 
            fasttext.load_model(os.path.dirname(os.path.realpath(__file__))+"/models/discord_langdetect.ftz")
        ]
        self.reliable_min = reliable_min
        self.dictio = DictDetector()
    
    def fasttext_detect(self, text):
        output = []
        for model in self.fasttext_models:
            output.append(model.predict(text.lower(), k=5))
        
        result = []
        for i in range(len(output)):
            for l in range(len(output[i][0])):
                result.append((output[i][0][l].replace('__label__', ''), output[i][1][l]/2 if i == 1 else output[i][1][l]))

        return result

    def dict_detect(self, text):
        dictio_pred = self.dictio.detect(text.lower())
        return dictio_pred

    def lingua_detect(self, text):
        lingua_detection = self.lingua_detector.compute_language_confidence_values(text)
        result = []

        for lingua_output in lingua_detection:
            result.append((lingua_output[0].iso_code_639_1.name.lower(), lingua_output[1]))

        return result

    def clean_text(self, text):
        text = re.sub(r"[!\"#$%&\'()*+,\-.\/:;<=>?@\[\\\]^_`{|}~ ]{2,}", lambda match: match.group()[0] + (" " if " " in match.group() else ""), text)
        text = re.sub(r'(\w)\1{2,}', r'\1\1', text)
        text = re.sub(r'\d+|\^', '', text)
 
        s = "@#$<>[]*_-~&%+/§{}=\|:▬"
        for char in text:
            if char in s:
                text = text.replace(char, "", 1)
        
        text = emoji.replace_emoji(text, replace='').strip()

        return unicodedata.normalize("NFKC", text.replace('\n', ''))[:200]

    def verification(self, text, lang):
        if 'im' in text and len(text) < 50 and lang == 'de':
            return text.replace('im', "I'm", 1), False 

        return text, True

    def detect(self, text, recusrv=False):
        text = self.clean_text(text)
    
        if text == '':
            return 'en', False

        output = []

        output.extend(self.fasttext_detect(text))
        output.extend(self.lingua_detect(text))

        dictio_detection = self.dict_detect(text)
    
        if dictio_detection[1][1] == 1:
            return dictio_detection[1][0], True

        if len(set(text.lower())) <= 2:
            return 'en', 'False'

        output.extend(dictio_detection[0])

        top = {}
        for i in output:
            if i[0] in top:
                top[i[0]] = top[i[0]]+i[1]
            else:
                top[i[0]] = i[1]
       
        lang = max(top, key=top.get)

        if not recusrv:
            verif = self.verification(text.lower(), lang)
            if not verif[1]:
                return self.detect(verif[0], True)
            
        return lang, True if top[lang]/4 >= self.reliable_min else False
