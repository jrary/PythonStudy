import sys
M = []
N = int(sys.stdin.readline())
visited = []
direction = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0)
]
count = 0
vil_num = []

def dfs(p):
    global count
    count += 1
    x, y = p[0], p[1]
    visited[x][y] = 1
    for d in direction:
        nx, ny = x+d[0], y+d[1]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] == 0 and M[nx][ny] == 1:
                dfs((nx, ny))

for _ in range(N):
    M.append(list(map(int, sys.stdin.readline().strip())))
    visited.append(list(0 for _ in range(N)))


for i in range(N):
    for j in range(N):
        if M[i][j] == 1 and visited[i][j] == 0:
            dfs((i, j))
            vil_num.append(count)
            count = 0

vil_num.sort()
print(len(vil_num))
for n in vil_num:
    print(n)