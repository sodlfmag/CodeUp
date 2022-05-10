min = 10000000000
n = int(input())
students = list(map(int, input().split()))
for i in students:
    if min > i:
        min = i
print(min)