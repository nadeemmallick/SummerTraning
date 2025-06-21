import numpy as np

A = np.array([[4, 7], [2, 6]])

I = np.eye(A.shape[0])

A_inv = np.linalg.solve(A, I)

print("Original Matrix A:")
print(A)

print("\nIdentity Matrix I:")
print(I)

print("\nInverse of A:")
print(A_inv)
