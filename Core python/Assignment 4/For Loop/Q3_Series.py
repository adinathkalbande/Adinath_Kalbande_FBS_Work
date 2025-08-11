#WAP to print sum of series upto n.
num = int(input("Enter number = "))
sum = 0

for i in range (1, num):
    sum += i
    i += 1
print(f"Sum of Series = {sum}")