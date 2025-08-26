#Write a program to create a duplicate of an existing list. It should not point to same list.
li = [12, 45, 67, 89, 23, 45, 68]
new_li = []

for i in li:
    new_li.append(i)

print(f'Existing list = {li}')
print(f'New list = {new_li}')
print(f'Memory location = {id(li)} and {id(new_li)}')