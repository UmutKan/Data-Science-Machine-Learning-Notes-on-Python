# https://github.com/atilsamancioglu/PythonForDataScienceNotebooks/blob/main/9-IntroToMatplotlib.ipynb
import numpy as np
import matplotlib.pyplot as plt

agelist = [10,20,30,30,30,40,50,60,70,75]
weightlist = [20,60,80,85,86,87,70,90,95,90]

plt.plot(agelist, weightlist, "y") # "y" --> colour yellow
plt.xlabel("AGE")
plt.ylabel("WEIGHT")
plt.title("Age vs. Weight")
plt.show()

#plt.savefig('plot_test.png') # SAVES AS AN IMAGE

np_age_list = np.array(agelist)
np_weight_list = np.array(weightlist)

plt.plot( np_age_list, np_weight_list, "r")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.show()

numpy_arr1 = np.linspace(0,10,20) # returns evenly spaced numbers in an interval
#print( "numpy_arr1: \n ", numpy_arr1 )
numpy_arr2 = numpy_arr1 ** 3

plt.plot(numpy_arr1, numpy_arr2 ,"g*--")
plt.show()

plt.subplot(1,2,1) # 1 row, 2 coloumn, first graph
plt.plot(numpy_arr1, numpy_arr2, "r*-")
plt.subplot(1,2,2)
plt.plot(numpy_arr2, numpy_arr1, "g--")
plt.show()

my_figure = plt.figure()
figure_axis = my_figure.add_axes([0.1,0.1,0.3,0.3])
figure_axis.plot(numpy_arr1,numpy_arr2, "g")
figure_axis.set_xlabel("X axis")
figure_axis.set_ylabel("Y axis")
figure_axis.set_title("Graph Title")
plt.show()

new_fig = plt.figure(dpi= 100)
new_axes = new_fig.add_axes( [0.1,0.1,0.9,0.9])
new_axes.plot(numpy_arr1, numpy_arr1 ** 2, label= "numpy array ** 2")
new_axes.plot(numpy_arr1, numpy_arr1 ** 3, label= "numpy array ** 3")
new_axes.legend() # shows info || .legend(loc= )
plt.show()