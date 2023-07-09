import sys
N, M = map(int, sys.stdin.readline().split())
milage = []
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)
    if len(arr) < L:
        milage.append(1)
    elif L != 1 and arr[L-2] == arr[L-3]:
        milage.append(arr[L-2])
    elif L == 1 and arr[0] == 36:
        milage.append(36)
    else:
        milage.append(arr[L-1]+1)
print(milage)
milage.sort()
now_milage = 0
for i in range(N):
    now_milage += milage[i]
    if now_milage > M:
        print(i)
        break