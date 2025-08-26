#Write a program to remove all occurrences of a given element in the list.
li = [2, 4, 6, 2, 3, 9, 2, 8, 7]
num = 2
new_list = []

for i in li:
    if i != num:
        new_list.append(i)

print(new_list)
