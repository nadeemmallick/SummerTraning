#Write a program to check whether the given input number is prime or not. The function has to return"True" if number is prime and return "False" in other cases.

def is_prime(number):

    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):

        if number % i == 0:
            return False
        
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("True")   # Prime
    
else:
    print("False")  # Not Prime