#quadratic equation
a = int(input("Enter value of a ="))
b = int(input("Enter value of b ="))
c = int(input("Enter value of c ="))

sqrt=((b**2)-(4*a*c))**0.5
result1= (-b+sqrt)/2*a
result2= (-b-sqrt)/2*a

print(f"Result of quadratic equation = {result1} {result2}")