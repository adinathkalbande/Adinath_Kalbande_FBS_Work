# Count the number of spaces in a string (take input from user)
string = input('Enter string : ')
result = len([ch for ch in string if ch == ' '])
print('Number of spaces in string = ', result)