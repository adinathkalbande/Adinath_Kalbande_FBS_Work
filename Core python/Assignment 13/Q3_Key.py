# Python Program to Check if a Given Key Exists in a Dictionary or Not...
def dictionary(di, key):
    for i in di:
        if key in di:
            return 'Key exists in dictionary'
        else:
            return 'key does not exists in dictionary.'

di = {1:'Python', 2:'Data Science', 3:'Data analytics', 4:'Python Fullstack'}
key = int(input("Enter key = "))
res = dictionary(di, key)
print(res)