#Write a program to calculate the m to the power n using recursion.
def power(m,n):
    if n==0:
        return 1
    else:
        return m* power(m, (n-1))
    
m = int(input('Enter value of m = '))
n = int(input("Enter value of n = "))
res = power(m,n)
print(f'Power of {m} to the {n} = {res}')