#WAP to check if given number is Perfect Number.
num = int(input("Enter number = "))
i = 1
sum = 0

while (i < num):
    if num % i == 0:
        print(i)
        sum = sum+i
    i += 1 

if num == sum:
    print(f"{num} is Perfect no.")
else:
    print(f"{num} is not perfect no.")