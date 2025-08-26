# Write a program to create a new list from existing list which contains cube of each number of list.
li = [1, 2, 3, 4, 5,6, 7,8,9]
cube_li = []

for i in range(1, len(li)+1):
    cube_li.append(i**3) 

print(cube_li)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cube_li = [0] * len(li)   # make an empty list with 9 zeros

for i in range(len(li)):
    cube_li[i] = li[i] ** 3

print(cube_li)
