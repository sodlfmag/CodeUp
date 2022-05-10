def flip(val):
    if val == 1:
        return 0
    elif val == 0:
        return 1

table = []
for  i in range(19):
    col = list(map(int, input().split()))
    table.append(col)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        table[x-1][j] = flip(table[x-1][j])
    for j in range(19):
        table[j][y-1] = flip(table[j][y-1])

for i in range(19):
    for j in range(19):
        print(table[i][j], end=" ")
    print()