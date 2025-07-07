def find_maximum(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = find_maximum(a, b, c)
print("Maximum number is:", maximum)
