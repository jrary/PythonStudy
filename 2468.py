import sys
# 최대 재귀 깊이 변경
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
M = []
direction = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0)
]
K = 1
max_height = 0

def dfs(p):
    x, y = p[0], p[1]
    # 현재 구역 방문 처리
    visited[x][y] = 1
    # 좌우상하 차례대로 검사
    for d in direction:
        nx, ny = x+d[0], y+d[1]
        # 그래프 영역 안에 존재하는지
        if 0<=nx<N and 0<=ny<N:
            # 방문하지 않았고, 임계값 K 초과
            if visited[nx][ny] == 0 and M[nx][ny] > K:
                dfs((nx, ny))


for _ in range(N):
    M.append(list(map(int, sys.stdin.readline().strip().split())))
    # 최대 높이 값 찾기
    now_max_height = max(M[-1])
    if now_max_height > max_height:
        max_height = now_max_height

# 최대 안전 영역을 저장할 변수
max_num = 0
for d in range(max_height):
    # 임계값 설정
    K = d
    # 변수 초기화
    now_num = 0
    visited = []
    for _ in range(N):
        visited.append(list(0 for _ in range(N)))
    # 방문하지 않은 곳 전부 탐색
    for i in range(N):
        for j in range(N):
            # 방문하지 않았고 임계값 이상이라면 DFS 시작
            if visited[i][j] == 0 and M[i][j] > K:
                dfs((i, j))
                now_num+=1
    # 현재까지의 최대 안전 영역인지 계산
    if max_num < now_num:
        max_num = now_num
    
print(max_num)