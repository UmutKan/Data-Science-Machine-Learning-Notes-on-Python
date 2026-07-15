# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/17-FeatureEngineeringEDA.ipynb
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("17-googleplaystore.csv")
#print(df.columns,"\n", df.shape, df.info())

print(df.isnull().sum())

#column type conversion
# df["Reviews"] = df["Reviews"].astype(int)
print("\n", df["Reviews"].str.isnumeric().sum()) # 1 element preventing conversion

print( df[~df["Reviews"].str.isnumeric()] ) # with ~ dataframe prints false values

df_clean = df.copy()
# deleting non numeric row
df_clean = df_clean.drop(df_clean.index[10472]) 
# converting to int type
df_clean["Reviews"] = df_clean["Reviews"].astype(int)
#print(df_clean.describe(), df_clean.info())

#print( df_clean["Size"].unique() )

# M for megabyt. To convert everything, replace M with 000 since 1mb ~= 1000 kb
# and also remove 'k' from every string
df_clean["Size"] = df_clean["Size"].str.replace("M", "000")
df_clean["Size"] = df_clean["Size"].str.replace("k", "")
#print("\n", df_clean["Size"].unique() )

df_clean["Size"] = df_clean["Size"].replace("Varies with device", np.nan)

#convert to int type
df_clean["Size"] = df_clean["Size"].astype(float)
#print( df_clean["Size"] )

#print( df_clean["Installs"].unique(),"\n", df_clean["Price"].unique() )

# remove $ sign from 'Price'
df_clean["Price"] = df_clean["Price"].str.replace("$", "")

# replace + and , from 'Installs'
df_clean["Installs"] = df_clean["Installs"].str.replace("+", "")
df_clean["Installs"] = df_clean["Installs"].str.replace(",", "")

# ANOTHER METHOD TO MANIPULATE MULTIPLE COLUMNS
'''
chars_to_remove = ["+",",","$"]
cols_to_clean = ["Installs", "Price"]

for item in chars_to_remove:
    for cols in cols_to_clean:
        df_clean[cols] = df_clean[cols].str.replace(item, "",)
'''
#print( df_clean["Installs"].unique(),"\n", df_clean["Price"].unique() )
# Convert to type float/int
df_clean["Installs"] = df_clean["Installs"].astype(int)
df_clean["Price"] = df_clean["Price"].astype(float)

# convert dates to datetime64 object
df_clean["Last Updated"] = pd.to_datetime(df_clean["Last Updated"])


'''
df_clean["Day"] = df_clean["Last Updated"].dt.day
df_clean["Month"] = df_clean["Last Updated"].dt.month
df_clean["Year"] = df_clean["Last Updated"].dt.year
'''
 
# EDA

#print(df_clean[df_clean["App"].duplicated()])

df_clean.drop_duplicates(subset=["App"], keep='first', inplace=True)

print( df_clean["Android Ver"].dtype ) # 'object' | 'O'

# Find every column that is not object
numeric_features = [feature for feature in df_clean.columns if df_clean[feature].dtype != 'O'] 

# Find every column that is object
categorical_features = [feature for feature in df_clean.columns if df_clean[feature].dtype == 'O']
print(f'Columns that are not object {numeric_features} \nColumns that are object {categorical_features}')

# plt.figure(figsize=(15,10))
# for i in range(0, len(numeric_features)):
#     plt.subplot(2, 3, i+1)
#     sns.kdeplot(x= df_clean[numeric_features[i]], fill=True)
#     plt.xlabel(numeric_features[i])
#     plt.tight_layout()
# plt.show()

# plt.figure(figsize=(15,4))
# category = ["Type", "Content Rating"]
# for i in range(0, len(category)):
#     plt.subplot(2, 3, i+1)
#     sns.countplot(x=df_clean[category[i]])
#     plt.xlabel(category[i])
# plt.show()

# Top App Categories by Installment

#print( df_clean.groupby(["Category"])["Installs"].sum().sort_values(ascending= False) )

df_cat_install =  df_clean.groupby(["Category"])["Installs"].sum().sort_values(ascending= False).reset_index()
df_cat_install.Installs = df_cat_install["Installs"]/1000000000
print(df_cat_install)

# Top 10 Catagories by Installs
df2 = df_cat_install.head(10)
plt.figure(figsize=(10,5))
sns.barplot(x="Installs", y="Category", data=df2)
plt.show()

# Top 5 App in Categories
apps = ["GAME", "COMMUNICATION", "TOOLS", "PRODUCTIVITY", "SOCIAL"] 
df_app_category = df_clean.groupby(["Category", "App"])["Installs"].sum().reset_index()
print( df_app_category.sort_values("Installs", ascending=False) )

# for i, app in enumerate(apps):
#     df2 = df_app_category[df_app_category.Category == app]
#     df2 = df2.head(5)
#     #print(df2)

#     plt.subplot(3,2,i+1)
#     sns.barplot( data=df2, x="Installs", y="App" )
#     plt.title(app, size=20)

# plt.tight_layout()

# plt.show()

# 5 Rating Apps
rating_df = df_clean.groupby(["Category", "App", "Installs"])["Rating"].sum().sort_values(ascending=False).reset_index()
top_rated_apps = rating_df[rating_df["Rating"] == 5.0]

df_clean["Android Ver"] = df_clean["Android Ver"].replace("and up", "", regex= True)
df_clean["Android Ver"] = df_clean["Android Ver"].replace("Varies with device", "", regex= True).replace("W", "").replace("", np.nan)

df_clean = df_clean[df_clean["Android Ver"].str.contains("-") == False]

# Target Encoding Example
mean_genres_installs = df_clean.groupby(["Genres"])["Installs"].mean() / 1000000
mean_genres_installs = mean_genres_installs.to_dict()

df_clean["Genres Encoded"] = df_clean["Genres"].map(mean_genres_installs)
