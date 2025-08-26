#. Write a program to create three lists of numbers, their squares and cubes.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_li = []
square_li = []
cube_li = []

for i in range(1, len(li)+1):
    num_li.append(i)
    square_li.append(i**2)
    cube_li.append(i**3)

print(f"Number List = {num_li}")
print(f"Square list = {square_li}")
print(f'cube List = {cube_li}')
