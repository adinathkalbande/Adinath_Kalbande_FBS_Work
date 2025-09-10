# Python Program to count number of digits and letters in a string.
def countDigit(string):
    count = 0
    for ch in string:
        if '0' <= ch <='9':
            count += 1
    return count

def countLetter(string):
    count = 0
    for ch in string:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            count += 1
    return count

string = input("Enter String = ")
print(f'Digit = {countDigit(string)} and Letter = {countLetter(string)}')

