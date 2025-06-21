#Write a program to print all even number from 1 to 20 using a loop.Modify the above program to use continue statement to skip printint the number 10.

for i in range(1,21):
    if i%2 == 0:
        #if i == 10:       #skip the number 10
           # continue
        print (i)