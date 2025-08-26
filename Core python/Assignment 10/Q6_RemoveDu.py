#Write a program to remove duplicates from the list.
li = [2, 4, 6, 4, 8, 3, 2, 9, 7, 6, 5, 4]

new_li = []

for i in li:
    if i not in new_li:
        new_li.append(i)

print(new_li)
