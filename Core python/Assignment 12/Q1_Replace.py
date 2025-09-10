#Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replace_a(string):
    new_string = ''
    for char in string:
        if char == 'a':
            new_string += '$'
        else:
            new_string += char
    return new_string

string = input("Enter string = ")
result = replace_a(string)
print(result)