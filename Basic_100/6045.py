list1 = input().split()
a, b, c = list(map(int, list1))
sum = a + b + c
print(sum, "%.2f" % (sum / 3))