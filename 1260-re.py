import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
connect = []
for _ in range(m):
    connect.append(list(map(int, sys.stdin.readline().split())))
dfs_visit = [False for i in range(n)]
bfs_visit = [False for i in range(n)]
connect.sort()


def dfs(k):
    dfs_visit[k-1] = True
    print(k, end=' ')
    for i, j in connect:
        if i == k and not dfs_visit[j-1]:
            dfs(j)
        if j == k and not dfs_visit[i-1]:
            dfs(i)


def bfs(k):
    b = deque()
    b.append(k)
    bfs_visit[k-1] = True
    while b:
        v = b.popleft()
        print(v, end=' ')
        for i, j in connect:
            if i == v and not bfs_visit[j-1]:
                b.append(j)
                bfs_visit[j-1] = True
            if j == v and not bfs_visit[i-1]:
                b.append(i)
                bfs_visit[i-1] = True


dfs(v)
print()
bfs(v)
