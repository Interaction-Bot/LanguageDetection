import ShortLanguageDetection

detection = ShortLanguageDetection.Detector() # reliable_min=0.5 in arguments for less wrong detection.
print(detection.detect('ah'))