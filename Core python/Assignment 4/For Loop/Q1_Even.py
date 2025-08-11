#WAP to print all even numbers until n.
num = int(input("Enter Number = "))

print("Here is the even numbers until n :")
for i in range(1,num):
    if i % 2==0:
        print(i)