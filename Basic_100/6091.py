from tkinter import Y


def GCD(x,y):
    r = 1
    while r != 0:
        r = x % y
        if r == 0:
            return y
        x, y = y, r

def LCM(x,y):
    result = (x*y) // GCD(x,y)
    return result

a, b, c = map(int, input().split())
temp = LCM(a,b)
val = LCM(temp, c)
print(val)