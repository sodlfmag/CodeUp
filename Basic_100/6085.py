w, h, b = map(float, input().split())
result = ((((w * h * b) / 8.0) / 1024.0) / 1024.0)
print('%.2f'%result, 'MB')