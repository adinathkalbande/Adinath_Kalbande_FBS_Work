#Write a program to solve the following series : 
#a. 1! + 2! + 3! + 4! + …..n!

n = int(input("Enter number = "))
fact = 1
i = 1
sum = 0

while (i <= n):
    fact = fact*i
    print(fact)
    sum = sum+fact
    i+= 1
print(f"Sum of given factorial is = {sum}")