#WAP to check if a given number is prime number or not.
num = int(input("Enter any number = "))

for i in range (2,num):
    if (num % i ==0):
        print(f"{num} is not prime number.")
        break
else:
    print(f"{num} is prime number.")