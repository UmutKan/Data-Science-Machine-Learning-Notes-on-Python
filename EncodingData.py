# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/16-EncodingData.ipynb
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print( df[["class", "sex", "embark_town"]].isna().sum() )
# 2 na rows in embark_town so we drop them
df.dropna(subset=["embark_town"], inplace=True)

print( df[["class", "sex", "embark_town"]].isna().sum() ) # done 

''' One Hot Encoding '''

print(f'\ndf["class"].value_counts:\n {df["class"].value_counts()}')
print(f'\ndf["sex"].value_counts:\n {df["sex"].value_counts()}')
print(f'\ndf["embark_town"].value_counts:\n {df["embark_town"].value_counts()}')

df_onehot = pd.get_dummies(df, columns=["sex","embark_town"], drop_first=True)

''' Label Encoder '''

label_encoder = LabelEncoder() # CREATE OBJECT
df_label = df.copy()
 
df_label["sex"] = label_encoder.fit_transform(df_label["sex"])
#print(df_label)

''' Ordinal Encoder '''

df_ordinal = df.copy()
class_order = ["Third", "Second", "First"]
ordinal_encoder = OrdinalEncoder(categories= [class_order]) # CREATE OBJECT

df_ordinal["class"] = ordinal_encoder.fit_transform(df_ordinal[["class"]])
#print(df_ordinal)



fig, axes = plt.subplots(1,4,figsize=(15,7))
df["sex"].value_counts().plot(kind="bar", ax=axes[0], title="Original Catagorical")
df_label["sex"].value_counts().plot(kind="bar", ax=axes[1], title="Label Encoded")
df_onehot["sex_male"].value_counts().plot(kind="bar", ax=axes[2], title="One Hot Encoded")
df_ordinal["sex"].value_counts().plot(kind="bar", ax=axes[3], title="Ordinal Encoded")

plt.show()