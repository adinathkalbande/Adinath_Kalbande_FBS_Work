# Python Program to Remove the Characters of Odd Index Values in a String
def RemoveOddInd(string):
    result = ''
    for i in range (len(string)):
        if i % 2 == 0:
            result += string[i]
    return result

string = input('Enter string = ')
res = RemoveOddInd(string)
print(res)

