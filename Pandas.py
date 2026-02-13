import pandas as pd
"""
series = pd.Series([1, 2, 3, 4, 5])
s = pd.Series([90, 85, 88], index=["Math", "Physics", "CS"])
print(s)

print(series)

data = {
    "Name": ["John", "Lisa", "Mike", "Sarah", "David"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [90, 85, 88, 92, 87]
}
df=pd.DataFrame(data)
df.head()
print(df.tail())
print(df.columns)
print(df)
"""
titanic_data = pd.read_csv(r"D:\MACHINE LEARNING\practicals\DATASETS\Titanic-Dataset.csv")
"""
print("info")
print(titanic_data.info())
print("describe")
print(titanic_data.describe())
print("---")
print(titanic_data.head())
print(titanic_data.shape)
"""
"""
print(titanic_data[titanic_data["Age"]>30])
print("---"*20)
print(titanic_data["Age"],titanic_data["Fare"],titanic_data["Name"])
print("---"*20)
"""
"""
print(titanic_data["Sex"].value_counts().sum())
print("---"*20)
"""

"""
print(titanic_data.isnull().sum())
new_df = titanic_data.dropna(subset=["Age"])  # Use inplace=False to avoid modifying the original DataFrame
titanic_data["Age"].fillna(titanic_data["Age"].mean(), inplace=True)  # Fill NaN values with the mean age
print(titanic_data.isnull().sum())
titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0], inplace=True)  # Fill NaN values with the most frequent value in Embarked column
print(titanic_data.isnull().sum())
titanic_data["Cabin"].fillna("Unknown", inplace=True) 
print(titanic_data.isnull().sum()) # Fill NaN values with "Unknown" in Cabin column
print(titanic_data)
"""

print(titanic_data.duplicated().sum())
titanic_data.rename(columns={"Pclass":"Passenger Class"}, inplace=True)
print(titanic_data.columns)
titanic_data["Survived"] = pd.to_numeric(titanic_data["Survived"], errors="coerce")
print(titanic_data.dtypes)

print(titanic_data.groupby("Sex")["Fare"].mean())
