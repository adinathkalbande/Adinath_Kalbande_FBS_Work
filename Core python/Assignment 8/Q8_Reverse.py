#Write a program find reverse of a number
def reverseNo(num):
    temp = num
    rev_d = 0
    while temp > 0:
        d = temp % 10
        rev_d = rev_d*10 + d
        temp = temp // 10
    print(f"Reversed digit = {rev_d}")

num = int(input("Enter number = "))
reverseNo(num)
