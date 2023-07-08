import sys
N, M = map(int, sys.stdin.readline().split())
milage = []
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)
    print(L-1)
    milage.append(arr[L-1]-1)
milage.sort()
now_milage = 0
for i in range(N):
    now_milage += milage
    if now_milage > M:
        print(i+1)
        break
