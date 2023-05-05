from collections import deque
import sys
N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    line = sys.stdin.readline().strip()
    try:
        act, i = map(str, line.split())
        i = int(i)
    except:
        act = line
    if act == 'push':
        q.append(i)
    elif act == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif act == 'size':
        print(len(q))
    elif act == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif act == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif act == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
