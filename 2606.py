import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()


# Binary search
def find(start, end, k):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    if k < a[mid]:
        find(start, mid-1, k)
    elif k == a[mid]:
        print(1)
        return
    elif k > a[mid]:
        find(mid+1, end, k)


for i in b:
    find(0, len(a)-1, i)
