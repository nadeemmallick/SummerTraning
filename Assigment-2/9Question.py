#Create a 1D array with values [1,2,3,1,3,9,3,5] and replace the maximum value with 15.

import numpy as np

array = np.array([1, 2, 3, 1, 3, 9, 3, 5])   

max_value = np.max(array) 

array [array == max_value] = 15                  #

print("Modified array:", array)
