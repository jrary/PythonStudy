import sys
N, K = map(int, sys.stdin.readline().split())
li = []
for i in range(1, int(N**(1/2))+1):
    if N % i == 0:
        li.append(i)
        li.append(N//i)
li = set(li)
li = list(li)
li.sort()
if len(li) < K:
    print(0)
else:
    print(li[K-1])
