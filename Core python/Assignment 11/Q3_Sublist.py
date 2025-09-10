#  Python Program to Sort the List According to the Second Element in Sublist
def sortbysecondEle(li):
    for i in range(1, len(li)):
        for j in range(0, len(li)-1):
            if li[j][1] > li[j+1][1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

li = [[5,9],[9,8],[1,2],[4,5]]
res = sortbysecondEle(li)
print(res)