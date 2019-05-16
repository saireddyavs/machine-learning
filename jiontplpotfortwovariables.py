import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math


col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
#print(iris)

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]
sns.jointplot(x="petal_length",y="petal_width",data=iris_setosa,kind="kde")
plt.show()

