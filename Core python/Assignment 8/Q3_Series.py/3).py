# 1^1 + 2^2 + 3^3+ …… n^n
def power(n):
    total = 0
    for i in range (1, n+1):
        total+= i**i
    return total

n=int(input('Enter value of n = '))

result = power(n)

print(f"Total = {result}")

