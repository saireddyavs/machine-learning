import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


col=["age","year","lymp","result"];
haber=pd.read_csv("haberman.csv",names=col)
print(haber.head())
from sklearn.neighbors import KNeighborsClassifier
neigh=KNeighborsClassifier(n_neighbors=4)
neigh.fit(haber.iloc[:,:3],haber["result"])
test=[[30,64,1]]
test=pd.DataFrame(test)

print("predicted:",neigh.predict(test))

from sklearn import metrics
from sklearn.model_selection import train_test_split

haber1=pd.read_csv("haberman.csv")
x=haber.iloc[:,:3]
y=haber.iloc[:,3:]
#print(y.head())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
k_range=np.arange(1,40)

scores={}
list_of_scores=[]
for k in k_range:
	knn=KNeighborsClassifier(n_neighbors=k)
	knn.fit(x_train,y_train)
	pred=knn.predict(x_test)
	scores[k]=metrics.accuracy_score(y_test,pred)
	list_of_scores.append(metrics.accuracy_score(y_test,pred))

#s=sorted(list_of_scores)



