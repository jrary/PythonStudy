import sys
N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

visit = [False for _ in range(N)]
C = []
result = -1


for _ in range(M):
    C.append(list(map(int, sys.stdin.readline().split())))


def dfs(v, cnt):
    cnt += 1
    print(v)
    visit[v-1] = True
    if v == B:
        global result
        result = cnt
        return
    for i, j in C:
        if i == v and not visit[j-1]:
            dfs(j, cnt)
        if j == v and not visit[i-1]:
            dfs(i, cnt)


dfs(A, -1)
print(result)
