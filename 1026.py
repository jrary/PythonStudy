import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
res = 0
for i in range(n):
    res += a[i]*b[n-i-1]
print(res)
