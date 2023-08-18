import sys

N = int(sys.stdin.readline())
left = list(map(int, sys.stdin.readline().split()))

line = [-1 for _ in range(N)]
for i in range(N):
    count = left[i]
    for num in range(N):
        if line[num] != -1:
            continue
        if count == 0:
            line[num] = i+1
            break
        if line[num] == -1:
            count -= 1
            
for n in line:
    print(n, end=' ')