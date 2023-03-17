import sys
n, m = map(int, sys.stdin.readline().split())
a = {}
b = {}
c = []
for i in range(1, n+1):
    t = sys.stdin.readline().strip()
    a[i] = t
    b[t] = i
for _ in range(m):
    c.append(sys.stdin.readline().strip())
for i in c:
    if i.isdigit():
        print(a[int(i)])
    else:
        print(b[i])
