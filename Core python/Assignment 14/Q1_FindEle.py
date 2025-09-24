# Write a Python program to find elements in a given set that are not in another set.
def setEle(set1, set2):
    result = set()
    for ele in set1:
        if ele not in set2:
            result.add(ele)
    return result 

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 8, 9, 10, 12}
res = setEle(set1, set2)
print(res)