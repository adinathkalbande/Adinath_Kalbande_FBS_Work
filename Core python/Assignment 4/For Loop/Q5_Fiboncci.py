#WAP to print Fibonacci series upto n
num = int(input("Enter Number = "))
a = 0
b = 1

for i in range (0,num):
    print(a, end=" ")
    c = a+b
    a = b
    b = c