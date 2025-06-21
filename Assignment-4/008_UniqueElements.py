nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique = list(set(nums))
print("Unique elements:", sorted(unique))