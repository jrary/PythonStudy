import sys


def bt(dpt, now, i):
    if dpt == m:
        for i in range(dpt):
            print(now[i], end=' ')
        print()
        return
    for j in range(i, n+1):
        now.append(j)
        bt(dpt+1, now, j+1)
        now.pop()


n, m = map(int, sys.stdin.readline().split())
a = []
bt(0, a, 1)
