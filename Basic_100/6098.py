table = []
for i in range(10):
    col = list(map(int, input().split()))
    table.append(col)
x, y = 1, 1

while True:
    table[x][y] = 9
    if table[x][y + 1] == 2: #오른쪽에 먹이가 있는 경우
        table[x][y + 1] = 9
        break
    elif table[x][y + 1] == 0: #오른쪽이 빈 경우
        y = y + 1
    elif table[x][y + 1] == 1: #오른쪽에 벽이 있는 경우
        if table[x + 1][y] == 1: # 오른쪽, 아래에 동시에 벽이 있는 경우
            break
        elif table[x + 1][y] == 2: #아래쪽에 먹이가 있는 경우
            table[x + 1][y] = 9
            break
        else :                  # 아래쪽이 빈 경우
            x = x + 1

for i in range(10):
    for j in range(10):
        print(table[i][j], end=" ")
    print()
    
    