import json
import os 

class Detector:
    def __init__(self) -> None:
        self.language = {}
        
        for f in os.listdir(os.path.dirname(os.path.realpath(__file__))+'/dict'):
            file = open(os.path.dirname(os.path.realpath(__file__))+'/dict/'+f)
            self.language[f.replace('.txt', '')] = file.read().split('\n')

        self.top_languages = json.load(open(os.path.dirname(os.path.realpath(__file__))+'/languages.json'))

    def __str__(self) -> str:
        return self.language.keys()

    def detect(self, string):
        string = string.lower().split()
        score = dict()

        for k in self.language.keys():
            common = 0
            for v in string:
                if v in self.language[k]:
                    common += 1
            score[k] = common
        
        result = []
        for k in score:
            if score[k] != 0:
                result.append((k, score[k]/len(string)))
        
        score_sorted = dict(sorted(score.items(), key=lambda item: item[1]))
        top = max(list(score.values()))
        
        output = []
        for k in score_sorted.keys():
            if score[k] == top:
                output.append([k, 0 if k not in self.top_languages else self.top_languages[k]])

        output.sort(key=lambda x:x[1])
        output = [[i[0], top/len(string)] for i in output]

        return result, output[::-1][0]
