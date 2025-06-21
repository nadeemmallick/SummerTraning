import numpy as np

array = np.ones((5,6),dtype=float)
array[1:-1,1:-1]=0.0

print (array)

