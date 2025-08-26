# Write a program to print all numbers which are divisible by m and n in the list.
li = [12, 15, 16, 25, 18, 56, 45, 30, 24, 36]
m = 2
n = 3
new_li = []

for i in li:
    if i % m == 0 and i % n == 0:
        new_li.append(i)

print(new_li)