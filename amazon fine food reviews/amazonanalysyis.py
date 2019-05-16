
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

stop=set(stopwords.words("english"))
print(stop)