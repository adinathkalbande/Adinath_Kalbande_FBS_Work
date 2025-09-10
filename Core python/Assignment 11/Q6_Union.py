#Python Program to Find the Union of two Lists...
def unionList(li1, li2):
    result = []
    for i in li1:
        if i not in result:
            result.append(i)
    for j in li2:
        if j not in result:
            result.append(j)
    return result

li1 = [8, 9, 7, 6]
li2 = [5, 8, 6, 3]
res = unionList(li1, li2)
print(res)