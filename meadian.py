import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math


col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
print(iris)

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]
print("meadians")
print("setosa",np.median(iris_setosa["petal_length"]))
print("virginica",np.median(iris_virginica["petal_length"]))
print("versicolor",np.median(iris_versicolor["petal_length"]))
print("With some extra outlier")
print("setosa",np.median(np.append(iris_setosa["petal_length"],500)))
