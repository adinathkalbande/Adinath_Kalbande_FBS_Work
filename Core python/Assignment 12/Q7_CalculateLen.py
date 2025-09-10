# Python Program to Calculate the Length of a String Without Using a Library Function
def calculate_len(string):
    count = 0
    for ch in string:
        count+=1
    return count

string = input('Enter String = ')
res = calculate_len(string)
print('length of string = ',res)