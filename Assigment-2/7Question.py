#Create an array of numbers between 700 and 999 that are divisible by either 5 or 7.Total Number of elements in the expected output is 67

import numpy as np

arr = np.arange(700,1000)

divisible_by_5 = arr[arr % 5 == 0]
divisible_by_7 = arr[arr % 7 == 0]

result = np.union1d(divisible_by_5,divisible_by_7)

print(result)
print("Total element:",len(result))
