# 5. Python Program to Count the Number of Vowels in a String

def countVowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in string:
        if ch in vowels:
            count+=1

    return count

string = input("Enter string = ")
res = countVowels(string)
print('Number of vowels in string is = ', res)
