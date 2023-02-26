import sys
a, b, c = map(int, sys.stdin.readline().split())
res = -1
while (a+b*res) >= c*res:
    res += 1
print(res)
