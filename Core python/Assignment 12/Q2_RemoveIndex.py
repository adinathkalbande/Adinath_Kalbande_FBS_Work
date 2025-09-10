# Python Program to Remove the nth Index Character from a Non-Empty String
def removeInd(string, ind):
    result = ''
    for i in range(len(string)):
        if i != ind:
            result += string[i]
    return result

string = input("Enter string = ")
ind = int(input("Enter index you want to remove = "))
res = removeInd(string, ind)
print(res)

