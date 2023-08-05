import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque(i+1 for i in range(N))

while len(q) != 1:
    q.popleft()
    move = q.popleft()
    q.append(move)

print(q[-1])