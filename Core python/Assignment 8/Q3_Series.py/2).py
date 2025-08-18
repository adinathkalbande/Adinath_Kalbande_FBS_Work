# 1!+ 2! + 3! + 4!+….. + n!

def series_sum(n):
    fact = 1
    sum = 0
    for i in range (1, n+1):
        fact *= i
        sum += fact
    return sum

n = int(input("Enter value of n = "))
result = series_sum(n)
print(f"Sum of series is = {result}")
