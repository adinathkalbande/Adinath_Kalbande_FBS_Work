#Write a program to find sum of digits of a number.
def sumOfdigit(num):
    temp = num
    total = 0
    while (temp > 0):
        d = temp % 10 
        total += d
        temp = temp//10
    print(f"Sum of digit = {total}")

num = int(input("Enter number = "))
sumOfdigit(num)