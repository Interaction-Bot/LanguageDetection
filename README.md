# LanguageDetection

Language detector used by Interaction Bot.

# Method

We made detection by dictionary and with ngram based method with fastText.
We also made a language priority (made by counting the number of detected language by Interaction Bot in 24 hours).
With discord, you could also use the language of the discord user interface send by the api to determine if a input is reliable (when reliabe is false).

# Usage

Run the main.py file (you must dl the fasttext model with this command:   
```
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin # put it to model
```

```py
import detector


def detect(text):
    pred = detector.detect(text)
    return pred[0], True if pred[1] > 0.4 else False

print(detect('Hi'))
```

# Output

Language code | reliability

# Futur

We will add a command to report bad detection, so we will update the dictionary detection accordingly. (we also update the code because it is bad actually 😂).
