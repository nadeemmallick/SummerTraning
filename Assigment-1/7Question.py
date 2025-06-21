#Write a program that takes user input as a string of numbers separated by commas,convert them to integers and calculate their average.

input_string = input("Enter numbers separated by commas:")

total = 0
count = 0

parts = input_string.split(",")

for item in parts:

    num = int(item.strip())  # Convert to integer after stripping spaces
    total += num
    count += 1

average = total / count
print(parts)
print("The average is:", average)