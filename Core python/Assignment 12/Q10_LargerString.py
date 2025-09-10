# 10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
def lengthstr(string):
    count = 0
    for ch in string:
        count+=1
    return count
def largerString(str1, str2):
    len_1 = lengthstr(str1)
    len_2 = lengthstr(str2)
    if len_1 > len_2:
        return f'"{str1}" is Larger string.'
    elif len_2 > len_1:
        return f'"{str2}" is Larger string.'
    else:
        return f'Both string are equal.'
    
str1 = input('Enter first string = ')
str2 = input('Enter second string = ')
print(largerString(str1, str2))