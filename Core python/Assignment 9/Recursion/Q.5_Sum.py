#Write a program to find sum of n numbers using recursion.
def sum_n(num):
    if num == 0:
        return 0
    else:
        return num+ sum_n(num-1)
    
num= int(input("Enter number = "))
res = sum_n(num)
print(f"Sum of first {num} numbers is {res}")