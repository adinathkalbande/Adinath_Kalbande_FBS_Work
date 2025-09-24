# Python program to find the union of two lists without using set concepts.
def unioun(li1, li2):
    u = []
    for i in li1:
        for j in li2:
            if i not in u:
                u.append(i)
            if j not in u:
                u.append(j) 

    return u
li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]
res = unioun(li1, li2)
print(res)