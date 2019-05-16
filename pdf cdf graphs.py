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

#for iris_setosa
counts,bin_edges=np.histogram(iris_setosa["petal_length"],bins=10,density=True)
pdf=counts/(sum(counts))
print(pdf)
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.legend("")
plt.show()


#for iris_virginica
counts,bin_edges=np.histogram(iris_virginica["petal_length"],bins=10,density=True)
pdf=counts/(sum(counts))
print(pdf)
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.legend("2")
plt.show()


#for iris_versicolor
counts,bin_edges=np.histogram(iris_versicolor["petal_length"],bins=10,density=True)
pdf=counts/(sum(counts))
print(pdf)
print(bin_edges)


cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.legend("3")
plt.show()


sns.FacetGrid(iris,hue="type",height=4).map(sns.distplot,"petal_length").add_legend()
plt.show()

