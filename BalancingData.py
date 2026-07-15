# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/15-BalancingData.ipynb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE
# random seed
np.random.seed(42)

set1no = 900
set2no = 100

df1 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=set1no),
    "feature_2": np.random.normal(loc=0, scale=1, size=set1no),
    "target": [0] * set1no
})

df2 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=set2no),
    "feature_2": np.random.normal(loc=0, scale=1, size=set2no),
    "target": [1] * set2no
})

df = pd.concat([df1, df2]).reset_index(drop=True)

print(df["target"].value_counts())

'''
UPSAMPLING => UPSAMPLE MINORITY
DOWNSAMPLING => DOWNSAMPLE MAJORITY -- GENERALLY 'LESS' PREFERABLE
'''

df_minority = df[df["target"] == 1]
df_majority = df[df["target"] == 0]


df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority), random_state=42) # replace=True upsample ederken arrayin içindeki verileri rastgelere kopyalayarak sayısını arttırır
print( df_minority_upsampled.shape )

df_majority_downsampled = resample(df_majority, replace=True, n_samples=len(df_minority), random_state=42)
print( df_majority_downsampled.shape )

df_upsampled = pd.concat([df_majority, df_minority_upsampled])

print( df_upsampled["target"].value_counts() )

'''
SMOTE --Synthetic Minority Over-Sampling Technique-- 
generates synthetic instances of the minority class by interpolating between existing instances.
 '''
plt.figure(figsize=(15,7))
plt.subplot(1,2,1)
plt.scatter(df["feature_1"], df["feature_2"], c=df["target"])
plt.title("Without Upsample")

oversample = SMOTE() # create object
x, y = oversample.fit_resample(df[["feature_1", "feature_2"]], df["target"]) # x features, y targets

print(f'======= X(features) ===== \n {x}')
print(f'======= Y(tagets) ===== \n {y}')

oversample_df = pd.concat( [x,y],axis=1 )

plt.subplot(1,2,2)
plt.scatter(oversample_df["feature_1"], oversample_df["feature_2"], c=oversample_df["target"])
plt.title("SMOTE")
plt.show()