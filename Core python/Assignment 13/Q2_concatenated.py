# Python Program to Concatenate Two Dictionaries Into One...
def concatenate(di1, di2):
    result = {}
    for i in di1:
        result[i] = di1[i]

    for i in di2:
        result[i] = di2[i]

    return result

di1 = {1:'Python', 2:'Java', 3:'C'}
di2 = {4:'Node Js', 5:'HTML', 6:'Angular'}
res = concatenate(di1, di2)
print(res)