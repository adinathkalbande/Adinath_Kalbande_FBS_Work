#WAP to print Armstrong number in range.
n1 = int(input("Enter first number in range :" ))
n2 = int(input("Enter last number in range : "))

for i in range(n1,n2+1):
    order = len(str(i))
    sum = 0
    for digit in str(i):
        sum= sum+ (int(digit)**order)
    if i == sum:
        print(i) 


#WAP to find given number is Armstrong number or not.
num = int(input("Enter number = "))
temp = num
order = len(str(num))
sum = 0

while (temp > 0):
    d = temp % 10
    sum += (d ** order)
    temp = temp//10
if sum == num:
    print(f"{num} is Armstrong Number.")
else:
    print(f"{num} is not Armstrong number.")