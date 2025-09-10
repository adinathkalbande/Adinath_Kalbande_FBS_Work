# Python Program to Put Even and Odd elements of a List into two Different List.
def EvenOdd(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

li = [10, 20, 31, 45, 57, 60, 77, 80]
even_list, odd_list = EvenOdd(li)
print(f'Even number List = {even_list}')
print(f'Odd number List = {odd_list}')
