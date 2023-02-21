import sys


def binary_search(a, l, start, end):
    if start > end:
        return False
    m = (start+end)//2
    if a == l[m]:
        return True
    elif a > l[m]:
        return binary_search(a, l, m+1, end)
    else:
        return binary_search(a, l, start, m-1)


n1 = int(sys.stdin.readline())
x = []
x = list(map(int, sys.stdin.readline().split()))
x.sort()
n2 = int(sys.stdin.readline())
y = []
y = list(map(int, sys.stdin.readline().split()))
for i in y:
    print(1 if binary_search(i, x, 0, n1-1) else 0, end=' ')
