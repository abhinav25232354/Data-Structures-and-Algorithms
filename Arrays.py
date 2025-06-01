# There are two types of array
"""
1. 1D Array (Single-Dimensional Array)
2. 2D Array (Multi-dimentional Array)

There are two ways of initializing arrays in python for now
1. Python Inbuilt Lists
2. Using Numpy library (Uses consistent memory allocation of the values)
"""


# Inbuilt List(Array) of Python
traditional_single_dimentional_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # A Linear List
traditional_multi_dimentional_array = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]] # Vector space of 5x2 matrix

# Numpy Array
import numpy as np

numpy_single_dimentional_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numpy_multi_dimentional_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])


for i in traditional_single_dimentional_array:
    print(i)
for i in traditional_multi_dimentional_array:
    print(i)

for i in numpy_single_dimentional_array:
    print(i)
for i in numpy_multi_dimentional_array:
    print(i)