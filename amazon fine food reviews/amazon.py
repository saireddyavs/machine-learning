
import sqlite3
import pandas as pd
import numpy as np
import nltk
import string
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import roc_curve,auc
from nltk.stem.porter import PorterStemmer

con=sqlite3.connect("database.sqlite")
filterd_data=pd.read_sql_query("select * from Reviews where Score!=3",con)
#df=pd.read_csv("Reviews.csv")
#print(df.shape)
#print(filterd_data.shape)
def partition(x):
    if x<3:
        return "negative"
    else :
        return "positive"
actualscore=filterd_data["Score"]
positivenegative=actualscore.map(partition)
filterd_data["Score"]=positivenegative


sorted_data=filterd_data.sort_values("ProductId",axis=0,ascending=True)
final=sorted_data.drop_duplicates(subset={"UserId","ProfileName","Time","Text"},keep="first",inplace=False)
final=final[final.HelpfulnessDenominator>=final.HelpfulnessNumerator]
count_vect=CountVectorizer()#in scikit-learn
final_counts=count_vect.fit_transform(final["Text"].values)

import re #regular expressions
import string
from nltk.corpus import stopwords

stop=set(stopwords.words(("english")))
#print(stop)
sno=nltk.stem.SnowballStemmer("english")
def cleanhtml(sentence):
    cleanr=re.compile('<.*>')
    cleantext=re.sub(cleanr,'',sentence)
    return cleantext
def cleanpunc(sentence):
    cleaned=re.sub(r'[?|!|\'|"|#]',r' ',sentence) #seee \' and combination
    cleaned=re.sub(r'[.|,|)|/|\]',r' ',cleaned)
    return cleaned
print(sno.stem("tasty"))#checking the rootword of tasty
sno=nltk.stem.SnowballStemmer("english")
i=0
str1=""
final_string=[]
all_positive_words=[]
all_negative_words=[]
s=""

print(sno)
for sent in final["Text"].values:
    filterd_sentence=[]

    sent=cleanhtml(sent)
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if((cleaned_words.isalpha())&(len(cleaned_words)>2)):
                if(cleaned_words.lower() not in stop):
                	s=(sno.stem(cleaned_words.lower())).encode("utf8")
                	filterd_sentence.append(s)
                	if(final["Score"].values[i]=="positive"):
                		all_positive_words.append(s)
                	else:
                		all_negative_words.append(s)
                else:
                	continue
            else:
             	continue

    str1=b" ".join(filterd_sentence)
    final_string.append(str1)
    i=i+1
final["cleaned_text"]=final_string



                    
            

    

