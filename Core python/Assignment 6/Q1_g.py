
for i in range (1,6):
    for j in range (1, 6-i):
        print(" ", end=" ")
    for j in range (1, 2*i):
        print(chr(65+j-1), end=" ")
    print()