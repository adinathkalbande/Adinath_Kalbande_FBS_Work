#WAP to print Fibonacci series upto n
num = int(input("Enter number = "))
a = 0
b = 1
count = 0

while (count < num):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count+=1

