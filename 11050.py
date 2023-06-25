import sys
N, K = map(int, sys.stdin.readline().split())
result = 1
for i in range(K):
    result *= (N-i)/(i+1)
print(int(result))