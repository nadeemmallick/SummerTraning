#Fractional of any number n is represented by n! and equal to 123...(n-1)*n

num = int(input("Enter a number:"))
factorial = 1

if(num<0):
    print("Factorial of negative number ddoes not exist")

else:
    for i in range (1,num+1):
        factorial*=i
        
        print(factorial)
