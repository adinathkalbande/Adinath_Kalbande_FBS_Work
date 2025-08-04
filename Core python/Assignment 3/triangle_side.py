#trianlg side
a = int(input("Enter value of first side = "))
b = int(input("Enter value of second side = "))
c = int(input("Enter value of third side = "))

if (a+b)>c and (b+c)>a and (a+b)>b:
    print("Triangle is valid.")
else:
    print("Ooops! Triangle is not valid.")