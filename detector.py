from lingua import Language, LanguageDetectorBuilder
import DictDetector
import langdetect
import fasttext
import re

model = fasttext.load_model("models/lid.176.bin")
model2 = fasttext.load_model("models/langdetect.ftz")
dictio = DictDetector.Detector()

languages = [
    Language.BULGARIAN,
    Language.CHINESE,
    Language.CROATIAN,
    Language.CZECH,
    Language.DANISH,
    Language.DUTCH,
    Language.FINNISH,
    Language.FRENCH,
    Language.GERMAN,
    Language.GREEK,
    Language.HINDI,
    Language.HUNGARIAN,
    Language.ITALIAN,
    Language.JAPANESE,
    Language.KOREAN,
    Language.LITHUANIAN,
    Language.NYNORSK,
    Language.POLISH,
    Language.PORTUGUESE,
    Language.ROMANIAN,
    Language.RUSSIAN,
    Language.SPANISH,
    Language.SWEDISH,
    Language.THAI,
    Language.TURKISH,
    Language.UKRAINIAN,
    Language.VIETNAMESE
]

detector = LanguageDetectorBuilder.from_languages(*languages).with_preloaded_language_models().with_low_accuracy_mode().build()

def detect(text):
    text = text.replace('\n', '').strip()
    text = re.sub(r'[^\w\s]', '', text)

    if text == '':
        return 'en', 1

    detection = model.predict(text.lower(), k=1)
    fasttext_pred = (detection[0][0].replace('__label__', ''), detection[1][0])

    if len(text) > 120:
        return fasttext_pred

    dictio_pred = dictio.detect(text.lower())
    if dictio_pred[1] == 1:
        return dictio_pred 
    
    lingua_detection = detector.compute_language_confidence_values(text)[0]
    lingua_detection = (lingua_detection.language.iso_code_639_1.name.lower(), lingua_detection.value)
 
    lang_detect = langdetect.detect_langs(text)[0]
    lang_detect = (lang_detect.lang, lang_detect.prob)

    detection = model2.predict(text.lower(), k=1)
    fasttext2_pred = (detection[0][0].replace('__label__', ''), detection[1][0])
   
    top = {}
    liste = [lingua_detection, lang_detect, fasttext_pred, fasttext2_pred, dictio_pred]

    for i in liste:
        if i[0] in top:
            top[i[0]] = top[i[0]]+i[1]
        else:
            top[i[0]] = i[1]

    language = max(top, key=top.get)
    return language, top[language]/len(liste)