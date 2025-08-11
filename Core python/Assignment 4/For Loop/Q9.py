#WAP to print all numbers in a range divisible by a given number.
num = int(input("Enter Number = "))
given_num = int(input("Enter number = "))

for i in range (1,num+1):
    if i % given_num == 0:
        print(i)
