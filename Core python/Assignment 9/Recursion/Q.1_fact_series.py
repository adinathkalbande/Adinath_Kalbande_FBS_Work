#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!

def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)
def fact_series(num):
    if num == 0:
        return 0
    else:
        return factorial(num)+ fact_series(num-1)

num = int(input("Enter number = "))
res = fact_series(num)
print(res)
