# Python Program to count number of lowercase characters in a string.
def lowercaseCount(string):
    count = 0
    for ch in string:
        if 'a' <= ch <= 'z' :
            count += 1
    return count

string = input('Enter string = ')
print('Lowercase = ',lowercaseCount(string))
