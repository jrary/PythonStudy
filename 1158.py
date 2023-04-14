import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
q = deque([i+1 for i in range(n)])
print('<', end='')
while True:
    if len(q) == 1:
        print(q[0], end='')
        break
    for _ in range(k-1):
        first = q[0]
        q.remove(first)
        q.append(first)
    print(q[0], end=', ')
    q.remove(q[0])
print('>', end='')
