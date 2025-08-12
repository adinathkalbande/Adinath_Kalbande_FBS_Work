#Write a program to solve the following series :
# x - x2/3 + x3/5 - x4/7 + …. to n terms 

x = int(input("Enter value of x = "))
n = int(input("Enter value of n = "))
total = 0

for i in range (1, n+1):
    term = (x*i)/(2*i-1)
    if i % 2 == 0:
        total -= term
    else:
        total += term

print(f"Total = {total}")
