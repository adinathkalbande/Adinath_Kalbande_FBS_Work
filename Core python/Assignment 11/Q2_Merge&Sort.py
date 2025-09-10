#Python Program to Merge Two Lists and Sort it.
def mergSort(li1, li2):
    merge_li = []
    for i in li1:
        merge_li.append(i)
    for j in li2:
        merge_li.append(j)
    return merge_li

def sortList(merge_li):
    for i in range(1, len(merge_li)):
        for j in range(0, len(merge_li)-1):
            if merge_li[j] > merge_li[j+1]:
                merge_li[j], merge_li[j+1] = merge_li[j+1], merge_li[j]
    return merge_li 

li1 = [7, 8, 3, 4, 2, 1,]
li2 = [6, 10, 14, 15, 23,]
merged_li = mergSort(li1, li2)
print('List before sorting = ', merged_li)
result = sortList(merged_li)
print('List after sorting = ', result)