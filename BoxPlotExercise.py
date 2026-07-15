# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/12-BoxPlotExercise.ipynb
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# box plot:
# median, quartile(25%, 50%, 70%), min-max 1.5 * IQR, outlier
'''
 Understanding Box Plots
 Box plots (also called whisker plots) are used to visualize the distribution of a dataset.
 They provide insights into:
- The median (Q2, 50th percentile)
- The interquartile range (IQR) - spread between Q1 (25th percentile) and Q3 (75th percentile)
- The minimum and maximum values within 1.5 * IQR (whiskers)
- Outliers (values outside the whiskers)
'''
# data = np.array([5, 7, 9, 15, 20, 22, 25, 30, 32, 35, 37, 40, 50, 55, 60, 100])
# plt.figure(figsize=(6,5))
# sns.boxplot(y=data)
# #plt.boxplot(x= data)
# plt.title("Box Plot")
# plt.ylabel("Data Value")
# plt.grid(True)
# plt.show()

df = sns.load_dataset("titanic") #Loads dataset available on Seaborn
#updated = df[df["fare"]<499] # to eliminate outlier
plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
sns.boxplot(x="class", y="age", data= df)
plt.title("Age by Class")
plt.xlabel("Class")
plt.ylabel("Age")

plt.subplot(1,2,2)
sns.boxplot(x="class", y="fare", data= df) # data= updated
plt.title("Fare by Class")
plt.xlabel("Fare")
plt.ylabel("Age")

plt.tight_layout()
plt.show()