import nltk
import numpy
import matplotlib

from nltk.book import *

sent1 = ['Call', 'me.', 'Ishmeal','.']

def testEndswith(sen):
    for x in sen:
        if x.endswith('l'):
            print(x)

def testCase(sen):
    for x in sen:
        if x.islower():
            print(x + ' islower')
        elif x.istitle():
            print(x + ' istitle')
        else:
            print(x + ' other')
print('text1: ')
print(text1)
print('text1.monstrous: ')
print(text1.similar("monstrous"))
text2.common_contexts(["monstrous", "very"])
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text3.generate('words')
