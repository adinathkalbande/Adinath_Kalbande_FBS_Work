# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set
def maxProduct(li):
    s = set(li)
    sort = sorted(s)

    max1 = sort[-2]*sort[-1]
    max2 = sort[0]*sort[1]

    if max1 > max2:
        ele_pair = sort[-2], sort[-1]
        product = max1
    else:
        ele_pair = sort[0], sort[1]
        product = max2
    return ele_pair, product
    
li = [4, 5, 2, 3, 8, 6, 7, 9, 1]
ele_pair, product = maxProduct(li)
print(f'The pair with maximum number is {ele_pair} and product is {product}.')
