import sys
from collections import deque

T = int(sys.stdin.readline())

def dfs(graph, visited, dir, y, x):
    stack = deque([(y, x)])
    visited[y][x] = 1
    while stack:
        ny, nx = stack.pop()
        for my, mx in dir:
            if [mx+nx, my+ny] in graph and visited[my+ny][mx+nx] != 1:
                stack.append((my+ny, mx+nx))
                visited[my+ny][mx+nx] = 1

def get_dfs(graph, m, n):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res = 0
    for x, y in graph:
        if visited[y][x] == 1:
            continue
        dfs(graph, visited, dir, y, x)
        res += 1

    return res

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph.append([x, y])
    
    print(get_dfs(graph, M, N))
