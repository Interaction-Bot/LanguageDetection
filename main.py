import DictDetector
import fasttext

text = "Hi"

dictio = DictDetector.Detector()

pretrained_lang_model = "lid.176.bin"
model = fasttext.load_model(pretrained_lang_model)

def detect(text):
    ngram_pred = model.predict(text, k=1)
    ngram_pred = (ngram_pred[0][0].replace('__label__', ''), ngram_pred[1][0])
    dictio_pred = dictio.detect(text)[0]
    
    if dictio_pred is not None:
        if dictio_pred[1] == 1:
            return dictio_pred[0], True
        elif ngram_pred[1] > 0.7:
            return ngram_pred[0], True 
        else:
            if dictio_pred[1] > 0.5 and dictio_pred[0] == ngram_pred[0]:
                return dictio_pred[0], True
    
    return ngram_pred[0], False if ngram_pred[1] < 0. else True 
    

print(detect(text.lower()))
