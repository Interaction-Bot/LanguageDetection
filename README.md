# Installation

`pip install ShortLanguageDetection`

# Usage

```py
import ShortLanguageDetection

detection = ShortLanguageDetection.Detector() # reliable_min=0.5 in arguments for less wrong detection.
print(detection.detect('text'))
# ('en', True)
```

# Project

This language detector is used by interaction bot to detect the language of message sent by user.
It has for objective to improve the language indentification for this type of message.

# Medium Post

https://medium.com/@jourdelune863/improving-language-detection-for-chat-discord-b148dfacc2e5

# Contribute

You can make pr or join this server for speaking about this detector: https://discord.gg/G8BjAV9hgg.
