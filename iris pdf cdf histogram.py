import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
print(iris)

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

print(iris_setosa.count())

plt.plot(iris_setosa["petal_length"],np.zeros_like(iris_setosa["petal_length"]))
plt.plot(iris_versicolor["petal_length"],np.zeros_like(iris_versicolor["petal_length"]))
plt.plot(iris_virginica["petal_length"],np.zeros_like(iris_virginica["petal_length"]))
plt.show()



sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"petal_length").add_legend()


sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"petal_width").add_legend()

sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"sepal_length").add_legend()

sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"sepal_width").add_legend()
plt.show()
