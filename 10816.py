import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().strip().split()))

a.sort()

h = {}
for i in a:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
for i in b:
    print(h[i] if i in h else 0, end=' ')
