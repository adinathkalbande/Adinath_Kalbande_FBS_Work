#Write a program to check whether a number is prime or not using recursion.
def check_prime(num, i=2):
    if num <= 1:
        return False
    elif i == num:
        return True
    elif num % i ==0:
        return False
    else:
        return check_prime(num, i+1)
    
num = int(input("Enter number = "))
if check_prime(num):
    print(f'{num} is prime number.')
else:
    print(f'{num} is Not prime number.')