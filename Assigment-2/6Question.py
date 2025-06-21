import numpy as np

array = np.arange(210,346)
array[array%10 == 0]=100

print(array)