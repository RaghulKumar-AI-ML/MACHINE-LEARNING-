import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('D:\MACHINE LEARNING\practicals\DATASETS\Titanic-Dataset.csv')

plt.plot(df["Fare"])# i chose fare because it is a continuous variable and it will show the trend of fare across the passengers
plt.xlabel("Index")
plt.ylabel("Fare")
plt.title("Fare of Passengers in Titanic Dataset")
plt.show()

plt.bar(df["Survived"].value_counts().index, df["Survived"].value_counts().values)
plt.xlabel("Survived")
plt.ylabel("Count")
plt.title("Distribution of Survived in Titanic Dataset")
plt.show()

plt.hist(df["Fare"].dropna(), bins=20)
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.title("Distribution of Fare in Titanic Dataset")
plt.show()

correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)
sns.heatmap(correlation_matrix,annot = True,cmap = 'coolwarm')
plt.title("Correlation Heatmap")
plt.show() 