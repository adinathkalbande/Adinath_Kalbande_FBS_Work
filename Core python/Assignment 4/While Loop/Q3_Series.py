#WAP to print sum of series upto n.
num = int(input("Enter number = "))
i = 1
sum = 0

while (i < num):
    sum += i
    i = i+1
print(f"Sum of series = {sum}")