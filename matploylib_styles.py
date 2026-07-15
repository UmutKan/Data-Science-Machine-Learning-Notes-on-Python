# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/10-MatplotlibStyles.ipynb
import numpy as np
import matplotlib.pyplot as plt

data1 = np.linspace(0,10,20)
data2 = data1 ** 2

my_fig, my_axis = plt.subplots()
#check types of my_fig & my_axis
my_axis.plot(data1, data2)
my_axis.plot(data2, data1)
plt.show()

(new_fig, new_axis) = plt.subplots()
new_axis.plot(data1, data1 + 2, color="blue", linewidth=1.0)
new_axis.plot(data1, data1 + 3, "y", linewidth=3.0)
new_axis.plot(data1, data1 + 4, "r", linestyle= "-.")

new_axis.plot(data1, data1 + 5, color="#04F8F8", linestyle= ":", marker="o", markersize=8, markerfacecolor="red")
new_axis.plot(data1, data1 + 4, "r", linestyle= "-.")
plt.show()

''' Scatter Plot '''
plt.scatter(data1,data2)
plt.show()

''' Histogram '''
new_arr = np.random.randint(0,100,50)
plt.hist(new_arr)
plt.show()

''' Box Plot '''
plt.boxplot(new_arr)
plt.show()