# There is a list with some numbers. Create a new dictionary using this list in such a way that key is number and value is frequency of occurences of that number in list.
# [1,3,4,1,2,3,6,7,1,2,4]
# [1:3:3:2:2:2]

def frequncy(li):
    freDict = {}
    for i in li:
        if i in freDict:
            freDict[i] += 1
        else:
            freDict[i] = 1
    return freDict 

li = [1,3,4,1,2,3,6,7,1,2,4]
res = frequncy(li)
print(res)