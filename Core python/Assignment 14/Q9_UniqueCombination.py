# Write a Python program to find all the unique combinations of 3 
# numbers from a given list of numbers, adding up to a target number
def uniqueComb(li, target):
    result = []
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            for k in range(j+1, len(li)):
                if li[i]+li[j]+li[k] == target:
                    triplet = sorted([li[i], li[j], li[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result 

li = [1, 2, 1, -1, 1, 2, 1]
target = int(input("Enter Target = "))
res = uniqueComb(li, target)
print(res)