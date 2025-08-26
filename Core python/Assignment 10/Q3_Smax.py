# Write a program to find the second largest element in the list.

li = [12, 56, 89, 34, 98, 32, 67, 45]

max = li[0]
smax = 0

for i in range(1, len(li)):
    if li[i] > max:
        smax = max 
        max = li[i]
    elif li[i] > smax:
        smax = li[i]

print(f'Second Largest Number is {smax}.')