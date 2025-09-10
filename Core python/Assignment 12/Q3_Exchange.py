# Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def exchangeString(string):
    if len(string) <= 1:
        return string
    
    first = string[0]
    last = string[-1]
    middle = string[1:-1]
    return last + middle + first

string = input("Enter String = ")
print(exchangeString(string))

