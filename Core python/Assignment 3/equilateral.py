#Check whether the trianlg is equilateral, isosceles of scalene triangle.

a = int(input("Enter first side of triangle = "))
b = int(input("Enter second side of triangle = "))
c = int(input("Enter third side of triangle = "))

if a==b and b==c and a==c:
    print("Triangle is equilateral")
elif a==b or b==c or a==c:
    print("Triangle is isosceles") 
else: 
    print("Triangle is scalene.")

