# #Write a program to solve the following series :
# S = a + a2 / 2 + a3 / 3 + …… + a10 / 10

a = int(input("Enter value of a = "))
s = 0
i = 1
for i in range (i, 11):
    s += (a*i)//i

print(f"Sum = {s}.")