import sys
n = int(sys.stdin.readline())
x = []

for i in range(n):
    x.append(list(sys.stdin.readline().split()))

x.sort(key=lambda a: a[0])

for i in x:
    print(i[0], i[1])
