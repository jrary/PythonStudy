import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort()
li.sort(key=lambda x: x[1])
for i in range(n):
    print(li[i][0], li[i][1])
