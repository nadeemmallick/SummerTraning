matrix = []
print("Enter 3x3 matrix values:")
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

row_sums = [sum(row) for row in matrix]
col_sums = [sum(matrix[i][j] for i in range(3)) for j in range(3)]
print("Row sums:", row_sums)
print("Column sums:", col_sums)