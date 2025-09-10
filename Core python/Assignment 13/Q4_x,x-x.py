# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)...
def dictionary(num):
    di = {}
    for i in range(1, num+1):
        di[i] = i*i
    return di

num = int(input('Enter Number = '))
res = dictionary(num)
print(res)