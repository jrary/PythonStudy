import sys


def getRank(a, n):
    rank = 1
    for i in range(len(a)):
        if a[i][0] > a[n][0] and a[i][1] > a[n][1]:
            rank += 1
    return rank


n = int(sys.stdin.readline())
c = []
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    print(getRank(c, i), end=' ')
