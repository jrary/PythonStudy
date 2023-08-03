import sys

P = int(sys.stdin.readline())
for p in range(P):
    li = list(map(int, sys.stdin.readline().split()))
    del li[0]
    count = 0
    q = []
    for children in li:
        q.append(children)
        idx = len(q) - 1
        while q[idx] < q[idx-1]:
            q[idx], q[idx-1] = q[idx-1], q[idx]
            idx -= 1
            count+=1
            if idx == 0:
                break
    print(p+1, count)     