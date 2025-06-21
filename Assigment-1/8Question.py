#You are given a list A of N integers. Your task is to write a program that prints "Odd" (without quotes) ifthe sum of all odd numbers present in the list is greater than sum of all the even numbers present in thelist. In all other cases, print "Even" (without quotes).


input_string = input("Enter the list of numbers separated by commas: ")

A = [int(x.strip()) for x in input_string.split(",")]

odd_sum = 0
even_sum = 0


for num in A:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if odd_sum > even_sum:
    print("Odd")
else:
    print("Even")