import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
def route(n, m, d):
    if n == 0:
        return arr[n][m]
    else:
        col = [m-1, m, m+1]
        fuel = []
        for ci in range(len(col)):
            if col[ci] >= 0 and col[ci] < M:
                if ci != d:
                    fuel.append(route(n-1, col[ci], ci))
        return min(fuel) + arr[n][m]

res = []
for m in range(M):
    res.append(route(N-1, m, -1))
print(min(res))