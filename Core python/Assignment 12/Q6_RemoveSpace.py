#Python Program to Take in a String and Replace Every Blank Space with Hyphen
def removeSpace(string):
    result = ''
    for ch in string:
        if ch == ' ':
            result += '-'
        else:
            result += ch
    return result

string = input('Enter String = ')
res = removeSpace(string)
print('String after replace spaces with hyphen = ', res)