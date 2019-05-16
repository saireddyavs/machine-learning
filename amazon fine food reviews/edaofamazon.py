import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Reviews.csv")
#plt.hist(df["Score"])
#plt.ylabel("number of reviews")
#plt.show()
#d=pd.Series(' '.join(df['Text']).lower().split()).value_counts()[:100]
#print(d)
#rint(df.columns)
numerator=df["HelpfulnessNumerator"]
denominator=df["HelpfulnessDenominator"]

sns.boxplot(data=df,x="Score",y="HelpfulnessDenominator")
plt.show()