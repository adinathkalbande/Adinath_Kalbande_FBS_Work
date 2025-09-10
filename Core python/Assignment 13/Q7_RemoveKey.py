# Python Program to Remove the Given Key from a Dictionary..
def removeKey(di):
    result ={}
    for i in di:
        if key != i:
            result[i] = di[i] 
    return result

di = {1:'Python', 2:'Java', 3:'C', 4:'Angular', 5:'HTML'}
key = int(input('Enter key = '))
res = removeKey(di)
print(res)