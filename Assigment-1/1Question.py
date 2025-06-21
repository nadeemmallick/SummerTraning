#Printing those number which is divisible either 5 or 7 whit range of 1 to 50 using while loop.

num = 1

while(num<=50):
    num+=1
    
    if(num%5==0 or num%7==0):
        print(num)
