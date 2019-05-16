import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
#b=np.arange(100,250,1)
iris=pd.read_csv("iris.xlsx",names=col)
#df=pd.DataFrame(iris,index=b)
#print(iris)
#print(df)

print("First five rows")
print(iris.head())
print("*********")
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")

print("no of samples available for each type")
print(iris['type'].value_counts())
print("*********")
print(iris.describe())


iris.plot(kind="scatter",x="sepal_length",y="sepal_width")


sns.set_style("whitegrid")
sns.FacetGrid(iris,hue="type",height=4).map(plt.scatter,"petal_length","petal_width").add_legend()
#plt.show()


sns.set_style("whitegrid")
sns.pairplot(iris,hue="type",size=3);
plt.show()

