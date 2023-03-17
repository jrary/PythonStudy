import sys
n, m = map(int, sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    a.append(sys.stdin.readline().strip())
a = set(a)
for _ in range(m):
    t = sys.stdin.readline().strip()
    if t in a:
        b.append(t)
b = set(b)
print(len(b))
b = list(b)
b.sort()
for i in b:
    print(i)
