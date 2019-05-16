import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels import robust
col=["age","year","lymp","result"]
haber=pd.read_csv("haberman.csv",names=col)
#print(haber)
result_1=haber.loc[haber["result"]==1]
result_2=haber.loc[haber["result"]==2]

print("*****lymp******")
print("mean of result_1",np.mean(result_1["lymp"]))
print("mean od result_2",np.mean(result_2["lymp"]))
print("meadian of result_1",np.mean(result_1["lymp"]))
print("meadian of result_2",np.mean(result_2["lymp"]))
print("standard deviation of result_1",np.std(result_1["lymp"]))
print("standard deviation of result_2",np.std(result_2["lymp"]))
print("percentiles of result_1",np.percentile(result_1["lymp"],np.arange(0,100,25)))
print("percentiles of result_2",np.percentile(result_2["lymp"],np.arange(0,100,25)))
print("median absolute deviation of result_1",robust.mad(result_1["lymp"]))
print("median absolute deviation of result_2 ",robust.mad(result_2["lymp"]))


print("*****age******")
print("mean of result_1",np.mean(result_1["age"]))
print("mean od result_2",np.mean(result_2["age"]))
print("meadian of result_1",np.mean(result_1["age"]))
print("meadian of result_2",np.mean(result_2["age"]))
print("standard deviation of result_1",np.std(result_1["age"]))
print("standard deviation of result_2",np.std(result_2["age"]))
print("percentiles of result_1",np.percentile(result_1["age"],np.arange(0,100,25)))
print("percentiles of result_2",np.percentile(result_2["age"],np.arange(0,100,25)))
print("median absolute deviation of result_1",robust.mad(result_1["age"]))
print("median absolute deviation of result_2 ",robust.mad(result_2["age"]))


print("*****year******")
print("mean of result_1",np.mean(result_1["year"]))
print("mean od result_2",np.mean(result_2["year"]))
print("meadian of result_1",np.mean(result_1["year"]))
print("meadian of result_2",np.mean(result_2["year"]))
print("standard deviation of result_1",np.std(result_1["year"]))
print("standard deviation of result_2",np.std(result_2["year"]))
print("percentiles of result_1",np.percentile(result_1["year"],np.arange(0,100,25)))
print("percentiles of result_2",np.percentile(result_2["year"],np.arange(0,100,25)))
print("median absolute deviation of result_1",robust.mad(result_1["year"]))
print("median absolute deviation of result_2 ",robust.mad(result_2["year"]))

