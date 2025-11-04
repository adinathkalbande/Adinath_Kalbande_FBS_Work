# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def Fibbonacci(num):
    a = 0
    b = 1
    while(num > 0):
        c = a+b
        # print(c)
        a = b 
        b = c
        yield c
res = Fibbonacci(10)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))


