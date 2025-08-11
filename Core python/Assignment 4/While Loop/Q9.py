#WAP to print all numbers in a range divisible by a given number.
num = int(input("Enter number = "))
given_num = int(input("Enter given number = "))
i = 1

while (i <= num):
    if i % given_num == 0:
        print(i)
    i+= 1