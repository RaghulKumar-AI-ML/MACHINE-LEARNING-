import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('D:\MACHINE LEARNING\practicals\DATASETS\Titanic-Dataset.csv')

#(line plot )plt.plot(df["Age"])
"""barchart
counts = df["Sex"].value_counts()
plt.bar(counts.index, counts.values)
plt.xlabel("Sex")
plt.ylabel("Count")
plt.title("Distribution of Sex in Titanic Dataset")
plt.show()
"""
#histogram
"""
plt.hist(df["Age"].dropna(), )
sns.histplot(df["Age"].dropna())
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Age in Titanic Dataset")
plt.show()
"""
#right and left skewed example (understanding skewness)
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Right-skewed data (lognormal is a classic right-skewed distribution)
right = np.random.lognormal(mean=0.0, sigma=0.6, size=5000)

# Left-skewed data: take a right-skewed distribution and mirror it
left = -np.random.lognormal(mean=0.0, sigma=0.6, size=5000)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].hist(right, bins=40, color="steelblue")
ax[0].set_title("Right-skewed (tail → right)")
ax[0].set_xlabel("value")
ax[0].set_ylabel("count")

ax[1].hist(left, bins=40, color="tomato")
ax[1].set_title("Left-skewed (tail → left)")
ax[1].set_xlabel("value")
ax[1].set_ylabel("count")

plt.tight_layout()
plt.show()

"""
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)
sns.heatmap(correlation_matrix,annot = True,cmap = 'coolwarm')
plt.title("Correlation Heatmap")
plt.show()
