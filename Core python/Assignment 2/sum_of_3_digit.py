#Find the sum of three-digit number.

num = int(input("Enter Three digit number = "))

temp = num

a = temp // 100
temp = temp % 100

b = temp // 10
temp = temp % 10

c = temp // 1
temp = temp % 1

sum = a + b + c

print(f"Sum = {sum}")