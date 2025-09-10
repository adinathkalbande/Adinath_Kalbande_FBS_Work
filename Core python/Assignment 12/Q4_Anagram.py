# Python Program to Detect if Two Strings are Anagrams
def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return 'String is not anagram, because length is not same.'
    
    dict1 = {}
    dict2 = {}
    for ch1, ch2 in zip(str1, str2):
        if ch1 in dict1:
            dict1[ch1] +=1
        else:
            dict1[ch1] = 1
        if ch2 in dict2:
            dict2[ch2] += 1
        else:
            dict2[ch2] = 1
    if dict1 == dict2:
        return 'String is anagram.'
    return 'String is not anagram.'

str1 = input("Enter first string = ")
str2 = input('Enter secong string = ')
result = checkAnagram(str1, str2)
print(result)