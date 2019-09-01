#! python3 - 

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#nltk: package for text analysis
import nltk
import tokenize
import codecs
import unicodedata
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#output French accents correctly
def convert_accents(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

nltk.download('stopwords')

### MAIN ###
    
#openfile
text_temp=codecs.open('text.txt','r','utf-8').readlines()

#put content in a list
text=[]
for word in text_temp:
    word=word.strip().lower()
    if word!="":
        text.append(convert_accents(word))


#use FreqDist to get the most frequents words
fdist = FreqDist()
for word in  text:
    fdist[word] += 1
print("BEFORE removing meaningless words")
print(len(fdist.items()))

#use stopwords to remove articles and other meaningless words
for sw in stopwords.words("french"):
     if sw in fdist:
        del fdist(sw)
print("AFTER removing meaningless words")
print(len(list(fdist.keys())))