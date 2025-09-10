# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary..
def countFrequency(string):
    di = {}
    word = string.split()
    for word in word:
        if word in di:
            di[word]+=1
        else:
            di[word] =1
    return di
            
string = "try try don't cry"
res = countFrequency(string)
print(res)