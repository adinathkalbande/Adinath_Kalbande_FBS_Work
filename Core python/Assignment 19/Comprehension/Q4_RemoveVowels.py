# Remove all of the vowels in a string (take input from user).
string = input('Enter string = ').lower()
vowels = 'aeiou'
result = ''.join([ch for ch in string if ch not in vowels])
print(result)