# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set. 
def missingSet(set1, set2):
    missing_set2 = set()
    missing_set1 = set()
    for ele in set1:
        if ele not in set2:
            missing_set2.add(ele)
    for ele in set2:
        if ele not in set1:
            missing_set1.add(ele)
    return missing_set2, missing_set1

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
missing_set2, missing_set1 = missingSet(set1, set2)
print('First missing set = ', missing_set2)
print('Second Missing Set = ', missing_set1)