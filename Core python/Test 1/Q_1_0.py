#Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:

l = int(input("Enter value of length = "))
b = int(input("Enter value of breadth = "))
r = int(input("Enter value of radius = "))
pi = 3.14

rect = l*b
semi_circle = 1/2*pi*r**2

total_area = rect + semi_circle
perimeter = 2 * l + b +(pi * r)
print(f"Area = {total_area} and perimeter of this figure is {perimeter}")