import sys
n = int(sys.stdin.readline())
meet = []
for _ in range(n):
    meet.append(list(map(int, sys.stdin.readline().split())))
meet.sort()
meet.sort(key=lambda x: x[1])
res = 1
now = 0
for i in range(n):
    if meet[i][0] >= meet[now][1]:
        now = i
        res += 1
print(res)
