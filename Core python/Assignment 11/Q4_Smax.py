#Python Program to Find the Second Largest Number in a List Using Bubble Sort
def bubbleSort(li):
    max = 0
    smax = 0
    for i in range(1, len(li)):
        for j in range(0, len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    max = li[-1]
    smax = li[-2] 
    return max, smax

li = [5, 7, 90, 8, 65, 34]
max, smax = (bubbleSort(li))

print("Max = ", max)
print("Smax = ", smax)
            