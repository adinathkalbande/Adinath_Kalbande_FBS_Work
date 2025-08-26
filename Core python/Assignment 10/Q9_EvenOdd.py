#Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
li = [12, 34, 67, 89, 78, 65, 45, 37, 97, 68]
even_li = []
odd_li = []

for i in li:
    if i % 2 == 0:
        even_li.append(i)
    else:
        odd_li.append(i)

print(f'Even Number List = {even_li}')
print(f'Odd Number List = {odd_li}')