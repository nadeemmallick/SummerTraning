import numpy as np

arange_np = np.arange(97,123 , dtype=int)

char_array = np.array([chr(i) for i in arange_np])

print(arange_np)
print(type(char_array),char_array)