import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
col=["age","year","lymp","result"]
haber=pd.read_csv("haberman.csv",names=col)
result_1=haber.loc[haber["result"]==1]
result_2=haber.loc[haber["result"]==2]

counts,bin_edges=np.histogram(result_1["lymp"],bins=10,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
print("pdfs",pdf)
print("cdfs",cdf)
print("counts",sum(counts))
print("bin_edges",bin_edges)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.show()

sns.FacetGrid(haber,hue="result",height=4).map(sns.distplot,"age").add_legend()
plt.show()


