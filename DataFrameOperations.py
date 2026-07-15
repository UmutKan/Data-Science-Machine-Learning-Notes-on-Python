import numpy as np
import pandas as pd


def salary_catagory(salary):
    if salary < 50000:
        return "LOW"
    elif 50000 <= salary < 80000:
        return "MEDIUM"
    else:
        return "HIGH"
    
weather_df = pd.read_excel('6-weather.xlsx')

print(weather_df, "\n")
print(weather_df.describe()) 

#weather_df.isna() boş hücre var mı
#weather_df.head() kullanılarak ilk 5 element 
#weather_df.tail() kullanılarak son 5 element listelenir

'''     WORKING WITH MISSING DATA       '''

weather_na_df = pd.read_excel('6-weatherna.xlsx')
print("WEATHER NA INFO: \n")
print(weather_na_df.info(), "\n")

print("WEATHER NA: \n")
print(weather_na_df,"\n")
print("WEATHER NA paris.isna: \n")
print(weather_na_df['Paris'].isna())

print(weather_na_df.dropna()) # NaN rowlarını siler,axis=1 column için , inplace=True denirse kendini günceller
print(weather_na_df.drop('Paris',axis=1), "\n")

# weather_na_df.fillna('DOLDUR')  := Boş hücreleri verilen değerle doldurur

print( weather_na_df.mean(), "\n" )
print(weather_na_df.fillna(weather_na_df.mean()))

'''     GROUP BY     '''

employee_df = pd.read_csv('6-employee.csv')

grouped_employee = employee_df.groupby('Department')
# type(grouped_employee)  =>  <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
print(grouped_employee.count())

print( grouped_employee.describe() )

'''     CONCAT    '''

df1 = pd.read_csv('7-concat_data1.csv')
df2 = pd.read_csv('7-concat_data2.csv')
print(df1,"\n", df2)
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)

'''     MERGE    '''

df_merge1 = pd.read_csv('7-merge_data1.csv')
df_merge2 = pd.read_csv('7-merge_data2.csv')
#print(df_merge1, "\n", df_merge2, "\n")

    # MERGE -- OUTER JOIN
df_merged_outer = pd.merge(df_merge1, df_merge2, on='Employee_ID', how='outer') # 'on=' => neyin üzerinden birleştirilecek
#print("\tOUTER JOIN MERGED TABLE: \n", df_merged_outer)                                                         # 'outer' her şeyi birleştirir

    #  MERGE -- LEFT JOIN
df_merged_left = pd.merge(df_merge1, df_merge2, on="Employee_ID", how='left') # 'left': 1. df'i esas alır ve 2. df'ten bilgilerle doldurur
#print("\tLEFT JOIN MERGED TABLE: \n", df_merged_left)

    #  MERGE -- RIGHT JOIN
df_merged_right = pd.merge(df_merge1, df_merge2, on="Employee_ID", how='right') 
#print("\tRIGHT JOIN MERGED TABLE: \n", df_merged_right)

    # MERGE -- INNER JOIN
df_merged_inner = pd.merge(df_merge1, df_merge2, on="Emplyoee_ID", how="inner") # 'inner': iki df'in kesişimini oluşurturur
# print("\tINNER JOIN MERGED TABLE: \n", df_merged_inner)

'''     APPLY    '''
df_apply = pd.read_csv("8-apply_function_data.csv")
print(df_apply.count(), df_apply.columns())

#df_apply["Salary_Catagory"] = df_apply["Salary"].apply(salary_catagory)
#print(df_apply)

# Lambda fonksiyonu ile apply
# df_apply["New_Performance_Score"] = df_apply.apply(
#     lambda row: row["Performance_Score"] + 1 if row["Experience"] > 10 else row["Performance_Score"], 
#     axis=1
# )

# print(df_apply)