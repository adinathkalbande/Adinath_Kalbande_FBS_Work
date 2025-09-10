# Write a program to create three lists of numbers, their squares and cubes
def squareCube(li):
    square = []
    cube = []
    for i in li:
        square.append(i**2)
        cube.append(i**3)
    return square, cube

li = [1, 2, 3, 4, 5,]
square, cube = squareCube(li)
print('Original list = ', li)
print('Square =', square)
print('Cube =',cube)
