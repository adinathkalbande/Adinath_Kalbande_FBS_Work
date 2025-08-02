#Write a program to reverse three-digit number.

num = int(input("Enter three-digit number = "))
temp = num

a = temp // 100
temp = temp % 100

b = temp // 10
temp = temp % 10

c = temp // 1
temp = temp %1

reversed_num = (c*100)+(b*10)+a
print(f"Reversed Number is {reversed_num}")
