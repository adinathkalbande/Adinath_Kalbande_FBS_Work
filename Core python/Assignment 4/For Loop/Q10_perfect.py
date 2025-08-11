#WAP to check if given number is Perfect Number.
num = int(input("Enter number = "))
sum = 0
for i in range (1, num):
    if num % i == 0:
        sum += i
if num == sum:
    print("Number is perfect.")
else:
    print("Number is Not perfect.")