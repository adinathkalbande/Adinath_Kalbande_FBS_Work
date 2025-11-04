# Find all of the words in a string that are less than 5 letters (take input from user).
string = input('Enter string = ').split()
result = [word for word in string if len(word) < 5]
print(result)