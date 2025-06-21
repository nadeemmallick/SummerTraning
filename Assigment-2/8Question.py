# Create two arrays A and B, Array A contains linearly spaced 10 values between 12 and 25Array B contains linearly spaced 10 values between 20 and 45 The output should be returned as a Multiplication of the mean of array A with array B.

import numpy as np

A = np.linspace(12, 25, 10)

B = np.linspace(20, 45, 10)

mean_A = np.mean(A)

output = mean_A * B

print("Array A:", A)
print("Array B:", B)
print("Mean of A:", mean_A)
print("Output:", output)
