import sys
x, y, w, h = map(int, sys.stdin.readline().split())
a = w-x
b = h-y
res = min(x, y, a, b)
print(res)