# Python Program to Sum All the Items in a Dictionary

def sum_dict(di):
    total = 0
    for i in di:
        total += di[i]
    return total

di = {1:10, 2:20, 3:30, 4:40}
res = sum_dict(di)
print('sum of all items in dictionary = ', res)