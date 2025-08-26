# Write a program to find maximum and minimum element in a list.

li = [56, 67, 44, 89, 23, 34, 97, 90, 34,65]

max = li[0]
min = li[0]

for i in range(1, len(li)):
    if li[i] > max:
        max = li[i]
    elif li[i] < min:
        min = li[i]
print(f'Maximum number of list is {max} and Minimum number is {min}')