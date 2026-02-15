#computing mean , median and mode manually
"""
data = [10, 20, 30, 40, 100]
nums=0
for i in data:
    nums+=i
mean=nums/len(data)
print("Mean:", mean)

#median
sorted_data = sorted(data)
if len(sorted_data) % 2 == 0:
    median = (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2
else:
    median = sorted_data[len(sorted_data) // 2]
print("Median:", median)

#mode
dict_count = {}
for i in data:
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1
mode = max(dict_count, key=dict_count.get)
print("Mode:", mode)

"""

#calculating variance and standard deviation manually
data2=[10, 20, 30, 40, 100]

mean2 =sum(data2)/len(data2)
variance =sum((i-mean2)**2 for i in data2)/len(data2)
print("Variance:", variance)
standard_deviation = variance**0.5
print("Standard Deviation:", standard_deviation)

print((70-40)//31.622)#just tried to calculate z score for 70 with mean 40 and standard deviation 31.622(standardized value) 
#computing correlation using pandas
import pandas as pd
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 4, 5, 6]
})
correlation = df.corr()
print(correlation)
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()