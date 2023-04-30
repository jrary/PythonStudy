from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

queue = deque([(0, 0)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

print(maze[N-1][M-1])
