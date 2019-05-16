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
print("means")
print("setosa",np.mean(iris_setosa["petal_length"]))
print("virginica",np.mean(iris_virginica["petal_length"]))
print("versicolor",np.mean(iris_versicolor["petal_length"]))
print("standard-deviations")
print("setosa",np.std(iris_setosa["petal_length"]))
print("virginica",np.std(iris_virginica["petal_length"]))
print("versicolor",np.std(iris_versicolor["petal_length"]))
print(math.sqrt(np.mean(((iris_versicolor["petal_length"])-np.mean(iris_versicolor["petal_length"]))*((iris_versicolor["petal_length"])-np.mean(iris_versicolor["petal_length"])))))

