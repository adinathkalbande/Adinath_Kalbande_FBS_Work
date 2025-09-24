# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value...
def sumPairEle(li):
    result = []
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]+li[j] == targetEle:
                result.append((li[i], li[j]))
    return result

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
targetEle = int(input('Enter Target Element = '))
res = sumPairEle(li)
print(f'Pairs with sum of {targetEle} = {res}')