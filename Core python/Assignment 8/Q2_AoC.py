#. Write a program to calculate area of circle

def areaOfCircle(r):
    pi = 3.14
    area = pi*r**2
    return area

r = int(input("Enter value of radius = "))

result = areaOfCircle(r)

print(f"Area of Circle = {result}.")