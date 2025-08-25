#Write a program to reverse a number using recursion
def reverseNum(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverseNum(num//10, rev*10+num%10)
    
num = int(input("Enter number = "))
res = reverseNum(num)
print(f'Reverse number = {res}')