import sys


def bt(dpt, now):
    if dpt == m:
        for i in range(dpt):
            print(now[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if i not in now:
            now.append(i)
            bt(dpt+1, now)
            now.pop()


n, m = map(int, sys.stdin.readline().split())
a = []
bt(0, a)
