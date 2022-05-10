h, b, c, s = map(float, input().split())
result = ((((h * b * c * s) / 8.0) / 1024.0) / 1024.0)
print('%.1f'%result, 'MB')