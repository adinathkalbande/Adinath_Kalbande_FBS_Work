#Python Program to Sort a List According to the Length of the Elements within the list.
def length(str):
    count=0
    for ch in str:
        count+=1
    return count

def lengthOfEle(li):
    for i in range(1,len(li)):
        for j in range(0, len(li)-1):
            if length(li[j]) > length(li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
    return li

li = ['Lioneee','Tiger','Elephant','Bull','Dog', 'Horses']
res = lengthOfEle(li)
print("Sorted list = ", res)