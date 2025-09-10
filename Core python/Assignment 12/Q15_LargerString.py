# Python Program to find larger string without using built-in functions.
def lenstring(string):
    count = 0
    for ch in string:
        count+=1
    return count

def larger_string(string1, string2):
    len_1 = lenstring(string1)
    len_2 = lenstring(string2)
    if len_1 > len_2:
        return f'{string1} is Larger than {string2}.'
    elif len_2 > len_1:
        return f'{string2} is Larger than {string1}.'
    else:
        return 'Both string are equal.'

string1 = input("Enter First String = ")
string2 = input('Enter Second String = ')

print(larger_string(string1, string2))