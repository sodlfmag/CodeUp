h, w = map(int, input().split())
table = [[0 for i in range(w)]for j in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            table[x-1][y+j-1] = 1
    elif d == 1:
        for j in range(l):
            table[x+j-1][y-1] = 1
for i in range(h):
    for j in range(w):
        print(table[i][j], end=" ")
    print()