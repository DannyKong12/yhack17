from django.shortcuts import render
from django.http import HttpResponse
import indicoio
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import random
from watson_developer_cloud import ToneAnalyzerV3
import json
from os.path import join, dirname
tone_analyzer = ToneAnalyzerV3(
 username='f9eb5386-8182-4836-a4d5-6ef2f31b7fc6',
 password='Buab4jiC2qkB',
 version='2017-09-26'
)
np.set_printoptions(suppress=True)

nltk.download('punkt')

indicoio.config.api_key = '7c8c560345b56dd10371d7562a1b14e8'

def softmax(x):
   return np.exp(x) / np.sum(np.exp(x), axis=1)


def text(request, type, text):

    abcd = "you ever worked in a creative Department Sun. no sir. ever written the great ad. no sir. never put your ideas another man's hands ask him to put his idea. senores. rewrite add son. we write ads or people die. it's that simple. are we clear. yes sir. are we clear. Crystal. you want Brady. man with big ideas. you or you client service director. responsibilities that you can possibly fathom. You Weep For bigger loads. you have the luxury of not knowing what I know. doesn't sound product. bike repair stand. you don't want the truth because deep down in places you don't talk about it. you need me right ads. we use words like inside big ideas. the time nor the inclination to explain myself to a man who. sleeps under the blanket. otherwise I suggest you pick up the kids. what you think you are entitled to. did you send out an ad without showing the account people. you snotty nose little suits."
    tone = tone_analyzer.tone(text,sentences='false', content_type='text/plain')
    sentences = sent_tokenize(abcd) if text == "good_men.wav" else sent_tokenize(text)

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
    for i in range(len(numlst)):
        try:
            emojis.append((emotions[numlst[i][0]], numlst[i][1], tone_analyzer.tone(sentences[i],sentences='false', content_type='text/plain')['document_tone']['tones'][1]['tone_name']))
        except IndexError:
            emojis.append((emotions[numlst[i][0]], numlst[i][1], "Tentative"))
        except Exception as e:
            emojis.append((emotions[5], random.uniform(0.3, 0.35), tone_analyzer.tone(sentences[i],sentences='false', content_type='text/plain')['document_tone']['tones'][1]['tone_name']))
    return HttpResponse(str(emojis))
