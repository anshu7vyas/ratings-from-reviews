__author__ = 'ANSHUL'

'''
########################################################################################
#This script is used for cleaning the data. Here are all the steps taken:
#1.Remove numericals.
#2.Remove puntuations.
#3.Remove stop words, using nltk.corpus stopwords
#4.Stem the words using nltk's PorterStemmer
#5.Balanced the dataset
########################################################################################
'''
import nltk
import string
from nltk import word_tokenize
import random
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter

"""removing numericals from the reviews."""
def removeDigits(review):
    return review.translate(None, string.digits)

"""removing punctuations from the review data"""
def removePunctuations(review):
    review = review.lower()
    review = review.translate(None, string.punctuation)
    return review
    
"""Removing the stop words using nltk.corpus's stopwords."""
def removeStopWords(review):
    stopSet = set(stopwords.words("english"))
    tokens = nltk.word_tokenize(review)
    woStopWords = lambda tok : tok not in stopSet
    return ' '.join(filter(woStopWords, tokens))

"""implementing the PorterAlgorithm for stemming of words, readily available in nltk."""
def stemWords(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(tok.decode('utf-8')) for tok in tokens]

"""Pipeline for all the steps taken."""
def preProcess(review):
    review = removeDigits(review)
    review = removePunctuations(review)
    review = removeStopWords(review)
    tokens = nltk.word_tokenize(review)
    tokens = stemWords(tokens)
    return ' '.join(tokens)

"""This method is used for balancing the dataset so that there are equal number of positives and negatives."""
def balance_df(df):
   print "\n##############################################"
   print "\nDown scaling the dataset to balance"
   print "\n##############################################"
   groups = df.groupby('LABEL')
   mydict =  groups['STARS'].agg('count').to_dict()
   key =  min(mydict, key= mydict.get)
   print mydict[key]

   dfList = []
   for name, group in groups:
       if name is key:
           dfList.append(group)
       else:
           rows =random.sample(group.index, mydict[key])
           newdf = df.ix[rows]
           dfList.append(newdf)
   return pd.concat(dfList)
