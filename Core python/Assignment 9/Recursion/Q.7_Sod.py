#Write a program to find sum of digits using recursion.
def sep(num):
    if num == 0:
        return 0
    else:
        return num%10+sep(num//10)
    

    
num = int(input("Enter number = "))
res = sep(num)
print(res)
