#WAP to print all integers upto n that aren’t divisible by 2 and 3.
num = int(input("Enter any number = "))

for i in range (1,num+1):
    if i % 2 !=0 and i % 3 !=0:
        print(i)
    i= i+1