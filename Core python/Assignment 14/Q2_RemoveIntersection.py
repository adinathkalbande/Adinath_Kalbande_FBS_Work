# Write a Python program to remove the intersection of a second set with a first set.
def intersection(set1, set2):
    result = set()
    for ele in set1:
        if ele not in set2:
            result.add(ele)
    return result 

set1 = {1, 2, 3, 4, 6}
set2 = {2, 3, 4, 5, 7}
res = intersection(set1, set2)
print(res)