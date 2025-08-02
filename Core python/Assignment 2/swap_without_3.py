#Write a program to swap two numbers without using third variable.

x = int(input("Enter value of x = "))
y = int(input("Enter value of y = "))

x = x+y
y = x-y
x = x-y

print(f"After swapping value of x is {x} and y is {y}.")