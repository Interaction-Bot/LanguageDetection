# LanguageDetection

Language detector used by Interaction Bot.

# Method

We made detection by dictionary and with ngram based method with fastText.
We also made a language priority (made by counting the number of detected language by Interaction Bot in 24 hours).
With discord, you could also use the language of the discord user interface send by the api to determine if a input is reliable (when reliabe is false).

# Usage

Run the main.py file (you must dl the fasttext model with this command:   
```
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
```

```py
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
```

# Output

Language code | reliability

# Futur

We will add a command to report bad detection, so we will update the dictionary detection accordingly. (we also update the code because it is bad actually 😂).
