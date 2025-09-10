# Python Program to Multiply All the Items in a Dictionary

def multiply(di):
    mul = 1
    for i in di:
        mul *= di[i]
    return mul

di = {1:10, 2:20, 3:30}
res = multiply(di)
print("Multiplication = ", res)