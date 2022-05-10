n = int(input())
call = list(map(int, input().split()))
for i in range(len(call)):
    print(call[-i-1], end=" ")