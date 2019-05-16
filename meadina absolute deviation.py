import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math
from statsmodels import robust


col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
#print(iris)

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]


print("Meadian absolute deviations")
print("setosa",robust.mad(iris_setosa["petal_length"]))
print("viriginica",robust.mad(iris_virginica["petal_length"]))
print("versicolor",robust.mad(iris_versicolor["petal_length"]))


