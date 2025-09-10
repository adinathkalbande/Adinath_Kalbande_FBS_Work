# Write a program to print list after removing even numbers.
def removeEven(li):
    li1 = []
    for i in range(0, len(li)):
        if li[i] % 2 != 0:
            li1.append(li[i])
    return li1

li = [11, 23, 44, 67, 88, 56, 91]
res = removeEven(li)
print('List after removing Even numbers =',res)
