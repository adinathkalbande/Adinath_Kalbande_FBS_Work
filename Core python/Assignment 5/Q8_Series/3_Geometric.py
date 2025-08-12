# Write a program to solve the following series :
# Find the sum of a geometric series from 1 to n where the common ratio is 2. 

n = int(input("Enter the value of n = "))
a = 1
r = 2
temp = a
total = 0
i = 1

while(i <= n):
    total+= temp
    temp = temp*r
    i += 1

print(f"Sum of geometric series 1 to n is {total}.")