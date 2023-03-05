import sys
sys.setrecursionlimit(10**9)


def postorder(r, n):
    if r > n:
        return
    mid = n+1

    for i in range(r+1, n+1):
        if tree[r] < tree[i]:
            mid = i
            break
    postorder(r+1, mid-1)
    postorder(mid, n)
    print(tree[r])


tree = []
while 1:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break
postorder(0, len(tree)-1)
