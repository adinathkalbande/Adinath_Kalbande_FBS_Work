#angle valid or not.

a1 = int(input("Enter value of first angle = "))
a2 = int(input("Enter value of second angle = "))
a3 = int(input("Enter value of third angle = "))

triangle = a1 + a2 + a3

if triangle == 180:
    print("Triangle is valid!")

else:
    print("Oops! Trianlge is not valid.")