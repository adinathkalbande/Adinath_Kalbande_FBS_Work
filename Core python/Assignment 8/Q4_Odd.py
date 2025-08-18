#Sum of all odd numbers between 1 to n
def SumOfOdd(n):
    total = 0
    for i in range (1, n+1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter value of n = "))

result = SumOfOdd(n)

print(f"Sum of odd number is = {result}")
        
        