import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


col=["age","year","lymp","result"];
haber=pd.read_csv("haberman.csv",names=col)
#print(haber)
result_1=haber.loc[haber["result"]==1]
result_2=haber.loc[haber["result"]==2]


print("pdf graph")
counts,bin_edges=np.histogram(haber["lymp"],bins=10,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
print("pdfs",pdf)
print("cdfs",cdf)
print("counts",sum(counts))
print("bin_edges",bin_edges)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.title("pdf and cdf")
plt.show()

print("box plot")

sns.boxplot(y="lymp",x="result",data=haber)
plt.show()
print("violin plot")
sns.violinplot(x="result",y="lymp",data=haber)
plt.show()

