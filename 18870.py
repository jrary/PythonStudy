import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
y = sorted(set(x))
y = {y[i]: i for i in range(len(y))}
for i in x:
    print(y[i], end=' ')
