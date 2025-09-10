# Python Program to Calculate the Number of Words and the Number of Characters Present in a String
def calculateWord(string):
    count = 0
    for ch in string:
        if ch == ' ':
            count +=1
    return count +1
def calculateChar(string):
    count = 0
    for ch in string:
        count += 1
    return count

string = input('Enter String = ')
print(f'Word = {calculateWord(string)} and Character = {calculateChar(string)}')