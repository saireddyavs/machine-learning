import pandas as pd
import numpy as np
import math
import operator

import warnings
warnings.filterwarnings("ignore")
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
from sklearn.neighbors import KNeighborsClassifier
neigh=KNeighborsClassifier(n_neighbors=4)
neigh.fit(iris.iloc[:,:4],iris["type"])
testSet = [[1.4, 3.6, 3.4, 1.2]]
test = pd.DataFrame(testSet)
print(test)
print("predicted:",neigh.predict(test))
print("neighbors",neigh.kneighbors(test))



# splitting the data into training and test sets (80:20)
from sklearn.model_selection import train_test_split
#iris1=pd.read_csv("iris.xlsx")

x=iris.iloc[1:,:3]
y=iris.iloc[1:,4:]
#print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#print(x_train.shape)
#print(y_test.shape)

k_range=np.arange(1,25)
from sklearn import metrics

scores={}
list_of_scores=[]
for k in  k_range:
	knn=KNeighborsClassifier(n_neighbors=k)
	knn.fit(x_train,y_train)
	pred=knn.predict(x_test)
	scores[k]=metrics.accuracy_score(y_test,pred)
	list_of_scores.append(metrics.accuracy_score(y_test,pred))

print(scores)

import matplotlib.pyplot as plt
plt.plot(k_range,list_of_scores)
plt.show()
