#Write a program to reverse the list.

li = [12, 44, 55, 67, 43, 98, 78 ]
rev_li = []

for i in range(len(li)-1, -1, -1):
    rev_li.append(li[i])

print(rev_li)

 