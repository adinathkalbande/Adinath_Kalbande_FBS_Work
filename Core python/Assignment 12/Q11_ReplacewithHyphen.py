# Python Program to replace every blank space with hyphen in a string.
def replace_with_Hyphen(string):
    result = ''
    for ch in string:
        if ch == " ":
            result+='-'
        else:
            result+= ch
    return result

string = input('Enter String = ')
print(replace_with_Hyphen(string))
