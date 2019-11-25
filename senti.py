import numpy as np
import pandas as pd
import seaborn as sns
from pylab import *
import gzip
import nltk
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob,Word,Blobber
from textblob.taggers import NLTKTagger

#
# lt=["I enjoy vintage books and movies so I enjoyed reading this book.  The plot was unusual.  Don't think killing someone in self-defense but leaving the scene and the body without notifying the police or hitting someone in the jaw to knock them out would wash today.Still it was a good read for me.",
#  "This book is a reissue of an old one; the author was born in 1910. It's of the era of, say, Nero Wolfe. The introduction was quite interesting, explaining who the author was and why he's been forgotten; I'd never heard of him.The language is a little dated at times, like calling a gun a &#34;heater.&#34;  I also made good use of my Fire's dictionary to look up words like &#34;deshabille&#34; and &#34;Canarsie.&#34; Still, it was well worth a look-see.",
#  "This was a fairly interesting read.  It had old- style terminology.I was glad to get  to read a story that doesn't have coarse, crasslanguage.  I read for fun and relaxation......I like the free ebooksbecause I can check out a writer and decide if they are intriguing,innovative, and have enough of the command of Englishthat they can convey the story without crude language.",
#  "I'd never read any of the Amy Brewster mysteries until this one..  So I am really hooked on them now."]
#

# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# print(wiki.tags)

# train = [
# ('I love this sandwich.', 'pos'),
# ('this is an amazing place!', 'pos'),
# ('I feel very good about these beers.', 'pos'),
# ('this is my best work.', 'pos'),
# ("what an awesome view", 'pos'),
# ('I do not like this restaurant', 'neg'),
# ('I am tired of this stuff.', 'neg'),
# ("I can't deal with this", 'neg'),
# ('he is my sworn enemy!', 'neg'),
# ('my boss is horrible.', 'neg')
# ]
# test = [
# ('the beer was good.', 'pos'),
# ('I do not enjoy my job', 'neg'),
# ("I ain't feeling dandy today.", 'neg'),
# ("I feel amazing!", 'pos'),
# ('Gary is a friend of mine.', 'pos'),
# ("I can't believe I'm doing this.", 'neg')
#  ]

# cl = NaiveBayesClassifier(train)
# print(cl.classify("it's good"))
# print(cl.accuracy(test))

data=pd.read_csv("C:/Users/maitr/Downloads/final_reviews.csv")
# #print(data.head())
lt=data.iloc[:,1].values
#print(x)
print(len(lt))

# print(lt[3])
# blob=TextBlob(lt[3])
# print(blob.sentiment)
#
# print(lt[4])
# blob=TextBlob(lt[4])
# print(blob.sentiment)
#
# print(lt[5])
# blob=TextBlob(lt[5])
# print(blob.sentiment)

# print(TextBlob("very good").sentiment)

print(lt[433])
blob=TextBlob(lt[433])
print(blob.sentiment)


polarity_list,subjectivity_list=[],[]
for i in range(len(lt)):
    blob = TextBlob(lt[i])
    polarity_list.append(blob.sentiment.polarity)
    subjectivity_list.append(blob.sentiment.subjectivity)
polarity_df = pd.DataFrame(polarity_list, columns=["colummn"])
polarity_df.to_csv('polarity_list.csv', index=False)

subjectivity_df = pd.DataFrame(subjectivity_list, columns=["colummn"])
subjectivity_df.to_csv('subjectivity_list.csv', index=False)
# print(polarity_list[:5])
# print(subjectivity_list[:5])

#Lets plot distribution of polarity
sns.set(color_codes=True)

# Polarity Distribution
sns.distplot(polarity_list)
show()