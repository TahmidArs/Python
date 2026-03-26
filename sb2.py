import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the dataset
df=pd.read_csv("Tips Dataset.csv")

print(df.head(10))
print(df.info)

#Getting statistical summary
print(df.describe())

#Displaying column names
print(df.columns)

#Creating correlation heatmap
numeric_corr = df.select_dtypes(include=[np.number]).corr()

sns.heatmap(numeric_corr, annot=True, fmt=".2f", cmap="YlGnBu")
plt.show()
#Displaying the plots
plt.show()