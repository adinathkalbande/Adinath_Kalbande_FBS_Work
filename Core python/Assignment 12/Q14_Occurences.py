# Python Program to count the occurrences of each word in a string.
def occurences(string):
    di = {}
    word = string.split()
    for word in word:
        if word in di:
            di[word]+=1
        else:
            di[word]=1
    return di
    
string = 'Python is fun and python is easy language.'
res = occurences(string)
print(res)