# Write a program to find sum of all elements of list

li = [12, 45, 67, 89, 23, 65, 43, 64]

sum = li[0]

for i in range(1, len(li)):
    sum += li[i]

print(f'Sum of all elements in list = {sum}')