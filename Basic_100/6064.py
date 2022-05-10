a, b, c = map(int, input().split())
if a <= b:
    min = a
else:
    min = b

if c <= min:
    min = c

print(min)