n = int(input())
call = map(int, input().split())
students = [0 for i in range(23)]

for i in call:
    students[i-1] += 1

for i in range(23):
    print(students[i], end=" ")