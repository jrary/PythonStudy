import sys

# DFS
def dfs(v):
    global ift
    visit_list[v] = 1
    # 현재 노드와 연결된 지점 모두 방문
    s = [v]
    while s:
        n = s.pop()
        # 현재 노드에 연결된 노드를 차례로 저장하는데,
        # 다음 노드를 저장하기 전에 먼저 현재 노드의 자식 노드 저장을 수행
        for n_next in graph[n]:
            if not visit_list[n_next]:
                visit_list[n_next] = 1
                s.append(n_next)
                ift+=1

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
