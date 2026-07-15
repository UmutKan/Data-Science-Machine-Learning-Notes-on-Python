# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/14-IntroToFeatureEngineering.ipynb
# click the link for more info
# Working with Missing Data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print( df.isnull().sum() ) #df.dropna(axis=1)

'''
Imputation:
Mean Imputation
'''
sns.histplot(df["age"], kde=True, color="r")
#plt.show()

df["age_mean"] = df["age"].fillna(df["age"].mean()) # mean imputation # çok outlier varsa median koymak daha uygun
print( df[["age_mean", "age"]] )

print( df[df["embarked"].isnull()] )
mode_value = df[df["embarked"].notna()]["embarked"].mode()[0]
print( mode_value )

df["embarked_mode"] = df["embarked"].fillna(mode_value) # embarked'ın eksikleri modu ile dolduruldu