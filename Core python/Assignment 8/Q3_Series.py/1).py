#Write a program to find sum of following series using functions :
# 1+ 2 + 3 + 4+….. + n

def sum (n):
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum

n = int(input('Enter value of n = '))
result  = sum(n)
print(f"Sum = {result}.")
    
