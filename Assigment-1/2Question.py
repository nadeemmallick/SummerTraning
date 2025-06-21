#Print multiplication table 0f 24,50 and 29 using loop.

for num in [24,50,29]:
    print("Table of:",num)
    
    for i in range(1,11):
        print(num,"x",i,"=",num*i)