# Python Program to Add a Key-Value Pair to the Dictionary
def dictionary(di):
    di[3] = 'c'
    return di

di = {1:'a', 2:'b'}
res = dictionary(di)
print(res)