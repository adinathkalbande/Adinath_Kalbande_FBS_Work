#WAP to check if given number Strong Number.
num = int(input("Enter number = "))
temp = num
sum = 0

while (temp > 0):
    d = temp % 10
    temp = temp//10
    fact = 1
    i = 1
    while (i <= d):
            fact = fact * i    
            i += 1
    sum+= fact

if num == sum:
    print(f"{num} is strong number.")
else:
    print(f"{num} is not strong number.")