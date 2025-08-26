#Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.
li = [12, 7, 34, 56, 78, 23, 98, 23, 79, 23, 77, 23]
n = int(input("Enter number = "))
count = 0
for i in li:
    if i == n:
        count+=1


if count > 0:
    print(f'Yes, {n} present is {count} times in list.')
else:
    print(f'No, {n} is not present in list.')