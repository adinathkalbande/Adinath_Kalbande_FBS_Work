# Find all of the numbers from 1–1000 that have a 6 in them
num = [x+10 for x in range(1, 1001) if '6' in str(x)]
print(num)