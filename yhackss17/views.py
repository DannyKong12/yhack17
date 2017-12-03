from django.shortcuts import render
from django.http import HttpResponse
import indicoio
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import random
np.set_printoptions(suppress=True)

nltk.download('punkt')

indicoio.config.api_key = '7c8c560345b56dd10371d7562a1b14e8'

def softmax(x):
   return np.exp(x) / np.sum(np.exp(x), axis=1)


def text(request, type, text):


    sentences = sent_tokenize(text)

    emotiondict = indicoio.emotion(sentences)

    d = {}
    for k in emotiondict[0]:
        d[k] = list(d[k] for d in emotiondict)

    df = pd.DataFrame(d, columns=d.keys())


    mat = np.matrix(df.values)*10

    softmat = softmax(mat).round(4)

    numlst = [[np.argmax(i), i[np.argmax(i)]] if i[np.argmax(i)]>=0.60 else 5 for i in softmat]
    emotions = ["Anger", "Joy", "Fear", "Sadness", "Surprise", "Neutral"]
    emojis = []
    for i in numlst:
        try:
            emojis.append((emotions[i[0]], i[1]))
        except Exception as e:
            emojis.append((emotions[5], random.uniform(0.3, 0.35)))
    return HttpResponse(str(emojis))
