import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


col=["age","year","lymp","result"];
haber=pd.read_csv("haberman.csv",names=col)
#print(haber)
result_1=haber.loc[haber["result"]==1]
result_2=haber.loc[haber["result"]==2]
#print(result_1)
#print(result_2)
print("no of samples of each type::")
print(haber["result"].value_counts())

haber.plot(kind="scatter",x="age",y="lymp")
sns.set_style("darkgrid")
#sns.FacetGrid(haber,hue="result",height=4).map(plt.scatter,"age","lymp").add_legend()
#sns.pairplot(haber,hue="result",height=3)
sns.boxplot(x="result",y="lymp",data=haber)
plt.show()


