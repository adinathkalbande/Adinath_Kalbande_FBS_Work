#1. A list contains the denominations as follows:
# D = [2000, 500, 200, 100, 50, 20, 10, 5] 
# Accept an amount from user and calculate how many minimum number of notes will be needed for that amount.

def denominations(d, amt):
    temp = amt
    li = []
    for i in range(0, len(d)):
        notes = temp // d[i]
        li.append(notes)
        temp = temp % d[i]
    return li

def total(li):
    total = 0
    for i in range(0,len(li)):
        total += li[i]
    return total
        
d = [2000, 500, 200, 100, 50, 20, 10, 5]
amt = int(input('Enter amount = '))
li = denominations(d, amt)
res = total(li)
print(f"The Minimum number of notes for {amt} = {res}")