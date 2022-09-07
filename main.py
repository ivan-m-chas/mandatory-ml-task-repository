from random import choice
import numpy as np
from re import split
def tokenize(s):
    text = split("[^а-яё]+", s.lower())
    if (text[0] == ""):
        text = text[1:]
    if (text[-1] == ""):
        text = text[:-1]
    return text

class Model: 
    def __init__(self):
        self.model = {}
        self.words = np.empty((0,), np.str_)

    def fit(self, text, k):
        for i in range(len(text)):
            self.words = np.append(self.words, [text[i]])
            t = []
            for j in range(min(i, k)):
                t += [text[i - j - 1]]
                if (tuple(t) in self.model):
                    self.model[tuple(t)] = np.append(self.model[tuple(t)], [text[i]])
                else:
                    self.model[tuple(t)] = np.array([text[i]], np.str_)

    def generate(self, prefix, k, sze):
        text = prefix
        for i in range(sze):
            t = []
            suggested_word = np.random.choice(self.words)
            for j in range(min(len(text), k)):
                t += [text[len(text) - j - 1]]
                if (tuple(t) not in self.model):
                    break
                suggested_word = choice(self.model[tuple(t)])
            text += [suggested_word]
        return text

