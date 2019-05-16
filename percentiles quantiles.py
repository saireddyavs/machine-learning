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
print("Quantiles")
print("setosa",np.percentile(iris_setosa["petal_length"],np.arange(0,100,25)))
print("virginica",np.percentile(iris_virginica["petal_length"],np.arange(0,100,25)))
print("versicolor",np.percentile(iris_versicolor["petal_length"],np.arange(0,100,25)))
print("With some extra outlier")
print("setosa",np.percentile(np.append(iris_setosa["petal_length"],500),np.arange(0,100,25)))

print("90th percentiles")
print("seatosa",np.percentile(iris_setosa["petal_length"],90))
print("virginca",np.percentile(iris_virginica["petal_length"],90))
print("versicolor",np.percentile(iris_versicolor["petal_length"],90))
