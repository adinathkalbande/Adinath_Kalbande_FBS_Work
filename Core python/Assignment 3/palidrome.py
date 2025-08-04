#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter Three Digit Number = "))
temp = num 

d1 = temp // 100
temp = temp % 100

d2 = temp // 10
temp = temp % 10

d3 = temp // 1

reversed_digit = (d3 * 100) + (d2 * 10) + d1

if num == reversed_digit:
    print("Number is Palindrone.")
else: 
    print("Number is not Palindrone.")