# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def uniqueWord(string):
    words = string.split()
    un_words = set(words)

    freq = {}
    for word in un_words:
        # if word not in un_words:
        freq[word] = words.count(word) 
    return freq

string = "try try don't cry"
res = uniqueWord(string)
print(res)