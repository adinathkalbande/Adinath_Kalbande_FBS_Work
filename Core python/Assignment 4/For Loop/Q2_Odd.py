#WAP to print all odd numbers until n.
num = int(input("Enter number = "))

for i in range (1,num):
    if (i % 2 != 0):
        print(i)