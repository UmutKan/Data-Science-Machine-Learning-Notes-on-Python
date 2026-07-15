import numpy as np

my_list=[10,20,30,40]
numpy_array = np.array(my_list)

print( type(numpy_array) )  # <class 'numpy.ndarray'>
print(numpy_array)          # [10 20 30 40]
print( np.random.random(3) )# [0.2542656  0.92625675 0.65926507]

my_list1=[1,2]
my_list2=[2,3]

np_array1 = np.array(my_list1)
np_array2 = np.array(my_list2)

print( my_list1 + my_list2 ) #[1, 2, 2, 3]
print(  np_array1 + np_array2 ) #[3 5]
#Arrayler toplarken uzunlukları aynı olmalı veya biri tek elemanlı olamlı

# ARANGE & INDEXING
# list(range(0,20,2)) => np.arange(0,20,2)

ist = list(range(0,20,2))
arran = np.arange(0,20,2)
print(f'Liste: {ist}\nnp.arange: {arran}')  # Liste: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
                                            # np.arange: [ 0  2  4  6  8 10 12 14 16 18]

print(arran[0],"||" ,arran[-1] ,"||" ,arran[2:10:3] ,"||", arran[::-1]) # 0 || 18 || [ 4 10 16] || [18 16 14 12 10  8  6  4  2  0]

print( np.random.randn(4,3) )   # [[-1.59012501  1.53241742 -1.0003885 ]
                                #  [-0.60612413  0.24034673  0.64127756]
                                #  [ 1.05261625 -0.53178143  0.00322288]
                                #  [-1.56246085 -1.5095032   1.08639669]]
# MATRICES W/ NUMPY
my_matrix = np.array([ [5,10], [15,20] ])
print(my_matrix.sum()) # 50

print( np.ones( (3,4) ), np.zeros( (5,4) ) )    # [[1. 1. 1. 1.]
                                                #  [1. 1. 1. 1.]
                                                #  [1. 1. 1. 1.]] [[0. 0. 0. 0.]
                                                #  [0. 0. 0. 0.]
                                                #  [0. 0. 0. 0.]
                                                #  [0. 0. 0. 0.]
                                                #  [0. 0. 0. 0.]]
# MATRIX ARITHMETIC

first_array = np.array( [[10,20], [30,40]])
second_array = np.array([[5,15], [25,35]])
print(first_array.shape) # (2,2)
# shape index ile kullanılabiliyor
print( f'aritmetik toplam:\n{first_array + second_array}' ) #aritmetik toplam:
                                                            #[[15 35]
                                                            # [55 75]]

print( f'aritmetik çarpım:\n{first_array * second_array}' )
                                                                        # aritmetik çarpım:
                                                                        # [[  50  300]
                                                                        #  [ 750 1400]]
# MATRIX MULTIPLICATION - dot product # 1.nin column sayısı 2.nin row sayısına eşit olamalı
print(f'Dot Product:\n{ first_array.dot(second_array) }') 
# Dot Product:
# [[ 550  850]
#  [1150 1850]]

'''NUMPY OPERATIONS'''

new_array = np.random.randint(1,100,20)
print(new_array)
print( new_array > 25)
print( new_array[new_array > 25])

# TRANSPOSE & RESHAPE
matrix_arr = np.array([[10,20],[20,30],[30,40]])
print(matrix_arr.shape)
print(matrix_arr.transpose(), matrix_arr.shape) # matrix_arr.transpose() => matrix_arr.T

rand_arr = np.random.random((6,1))
print(rand_arr.shape)
rand_arr = rand_arr.reshape(2,3)
print(rand_arr)
rand_arr = rand_arr.reshape(3,2)
print(rand_arr)

# Z-SCORE

data = np.array([10,12,13,15,18,25,100,105])
mean = np.mean(data)
std = np.std(data)
z_scores = (data - mean)/std
print(f'Mean = {mean}, STD = {std}, Z_SCORES = {z_scores}')
print(data[z_scores > 1])

# math equations
#2x + 3y = 8 & 5x + 7y = 19

A = np.array([[2,3],[5,7]]) # coefficients
B = np.array([8,19]) #constants
solution = np.linalg.solve(A,B)
print(solution)