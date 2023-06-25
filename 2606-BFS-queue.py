import sys
from collections import deque

# bfs
def bfs(v):
    global ift
    # Deque 사용
    q = deque([v])
    visit_list[v] = 1
    while q:
        n = q.popleft()
        for n_next in graph[n]:
            if not visit_list[n_next]:
                visit_list[n_next] = 1
                q.append(n_next)
                ift += 1

# 초기화
N = int(sys.stdin.readline())
L = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visit_list = [0] * (N+1)
global ift
ift = 0
for _ in range(L):
    a, b = list(map(int, sys.stdin.readline().split()))
    # graph를 미리 초기화 후, 양방향의 정보를 저장
    graph[a].append(b)
    graph[b].append(a)

# 함수 호출
bfs(1)
print(ift)
