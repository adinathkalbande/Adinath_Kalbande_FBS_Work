# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user).
sen = input('Enter sentence : ')
words = sen.split()
result = {word:len(word) for word in words}
print(result)
