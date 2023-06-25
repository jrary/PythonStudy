import sys

# DFS
def dfs(v):
    global ift
    visit_list[v] = 1
    # 현재 노드와 연결된 지점 모두 방문
    for i in graph[v]:
        if visit_list[i] == 0:
            ift+=1
            dfs(i)

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
dfs(1)
print(ift)
