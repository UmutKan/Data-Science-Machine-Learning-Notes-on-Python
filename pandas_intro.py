import pandas as pd
import numpy as np

grades = {"Atil": 50, "James": 60, "Lars": 30}
print( pd.Series(grades))

name= ["Atil","James", "Lars"]
grade = [50,60,70]
print( pd.Series(name))
print( pd.Series(data= grade, index= name))

# with numpy
numpy_arr = np.array([50,40,30,20])
print( pd.Series(numpy_arr))

#arithmetic
constest_result = pd.Series(data=[10,5,100],index=["Atil","James","Lars"])
constest_result2 = pd.Series(data=[20,50,10],index=["Atil","James","Lars"])

print(f' JAMES: {constest_result["James"]}')

final_result = constest_result + constest_result2
print(final_result)

different_series = pd.Series([20,30,40,50],["a","b","c","d"])
different_series2 = pd.Series([10,5,3,1],["a","c","f","g"])

print(different_series + different_series2)

# DATA FRAME
data = np.random.randint(50 ,size =(4,3)) # max 50 olacak şekilde 4x3 matrix
data_frame = pd.DataFrame(data)
print(type(data_frame))
print(data_frame)
print(type(data_frame[0]))
print(data_frame[0])

new_df = pd.DataFrame(data, index= ["Atil","Zeynep", "Atlas", "Mehmet"], columns= ["Salary", "Age", "Seniority"])
print(new_df)
print(f'Age:\n {new_df["Age"]}')
print(new_df[["Salary","Seniority"]],"\n")

print(new_df.loc["Zeynep"], "\n") # row printleme INDEX İLE YAPLIMAK İSTENİRSE = new_df.iloc[1]

print( new_df.iloc[:,1] ) # : => bütün rowları seç , 1. column'u al

new_df["Extra"] = 10
print(new_df, "\n")

new_df.drop("Extra", axis=1, inplace = True) # axis=1 column , axis=0(default) row
print(new_df, "\n")

new_df.loc["Atlas", "Salary"] = 100_000
print(new_df.loc["Atlas", "Salary"], "\n") # ya da new_df.loc["Atlas"]["Salary"]

print(new_df > 5)
print("\n", new_df[new_df > 5])
print("\n", new_df[new_df["Salary"] > 20])

reset_frame = new_df.reset_index() # kolay erişim için numaralandırma yapar
print("\n", reset_frame)

new_indices = ["Ati","Zey","Atl","Meh"]
new_df["NewIndex"] = new_indices
print("\n", new_df)

new_df.set_index("NewIndex", inplace=True)
print("\n", new_df)
print("\n", new_df.loc["Ati"])

# MULTI INDEX
first_index = ["Simpson","Simpson","Simpson", "South Park", "South Park", "South Park"]
inner_index = ["Homer", "Bart", "Marge","Cartman", "Kenny", "Kyle"]
zipped_index = list(zip(first_index, inner_index))

zipped_index = pd.MultiIndex.from_tuples(zipped_index)
print("\n", zipped_index)

sample_values = np.ones((6,2))
big_df = pd.DataFrame(sample_values, index= zipped_index, columns= ["Age","Salary"])
print("\n",big_df)

print("\n", big_df.loc["Simpson"].loc["Homer"])