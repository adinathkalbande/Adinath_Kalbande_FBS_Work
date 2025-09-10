#Print 1 to 100 in snakes and ladder pattern.
def Snakes_Ladder():
    board = []
    for i in range(9, -1, -1):
        row = []
        for j in range((i*10)+1, (i+1)*10+1):
            row.append(j)
        if i % 2 != 0:
            row.reverse()
        board.append(row)
    return board
    
res = Snakes_Ladder()
for row in res:
    print(row)


