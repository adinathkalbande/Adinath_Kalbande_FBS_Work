# Python Program to Find the Intersection of Two Lists...
def intersection(li1, li2):
    result = []
    for i in li1:
        if i in li2 and i not in result:
            result.append(i)
            
    return result

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]
res = intersection(li1, li2)
print('Intersection between two list = ', res)
