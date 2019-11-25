import numpy as np
import pandas as pd
import sklearn
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from pylab import *
import gzip
import nltk
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob,Word,Blobber
from textblob.taggers import NLTKTagger
from sklearn import preprocessing

data=pd.read_csv("C:/Users/maitr/Downloads/final_reviews.csv")
x=data.iloc[0:380,1].values
# print(type(x))
y=data.iloc[0:380,4].values
t=list(x)
# print(type(t))
p=list(y)
print(len(t))
f=zip(t,p)
f2=list(f)
print(f2)
print(len(f2))
x2=data.iloc[381:434,1].values
y2=data.iloc[381:434,4].values
t2=list(x)
p2=list(y)
z=zip(t2,p2)
z2=list(z)
# for s in range(10):
# x_train, x_test = model_selection.train_test_split(f2, test_size=0.2,random_state=100)
# print(x_train)
# print(len(x_train))
# print(len(x_test))

cl=NaiveBayesClassifier(f2)
print(cl)
for i in z2:
    # print(i)
    print(cl.classify(i))
print(cl.accuracy(z2))