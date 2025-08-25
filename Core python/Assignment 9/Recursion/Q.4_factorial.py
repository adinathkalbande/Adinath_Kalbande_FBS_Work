#Write a program to find factorial using recursion.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
num = int(input("ENter number = "))
res = factorial(num)
print(f'Factorial of {num} is {res}')