import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li = list(set(li))
li.sort()
for i in li:
    print(i, end=' ')
