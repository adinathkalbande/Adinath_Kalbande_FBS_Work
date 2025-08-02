#Write a program to swap two numbers using third variable.

a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))

c = a
a = b
b = c

print(f"After Swapping value of a : {a} and b : {b}")