# A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it. Before coming to class, she ensured that All the numbers occur an Even number of times. However, while coming to the class, one coin fell down and gotlost. She wants to find out the number on the missing coin.
# Inputs:
# The original number of coins and the actual number on each of the coins, separated by spaces.
# Output: The number on the missing coin
# Sample Input: 8
# 5 7 2 7 5 2 5
# Sample Output: 5

def coins(n):
    coins = []
    for i in range(n-1):
        num = int(input('Enter coins number = '))
        coins.append(num)
        
    for coin in coins:
        if coins.count(coin) % 2 !=0:
            break
    return coin
n = int(input('Enter Original number of coins = '))
res = coins(n)
print(res)