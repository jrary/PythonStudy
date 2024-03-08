import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    res = 1
    for i in range(N):
        res *= (M-i)
        res /= (i+1)
    print(int(res))
    