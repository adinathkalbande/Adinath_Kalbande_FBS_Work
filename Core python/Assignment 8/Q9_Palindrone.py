# Write a program to check if entered number is a palindrome or not.
def PalindroneNo(num):
    temp = num
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev*10+d
        temp = temp// 10
    return rev

num = int(input("Enter number to check Palindrone or Not = "))
result = PalindroneNo(num)

if result == num:
    print("Number is palindrone.")
else:
    print("Number is not Palindrone.")


