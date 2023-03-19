import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
pr = [i for i in range(m, n+1)]
for i in range(m, n+1):
    if i == 1:
        pr.remove(i)
        continue
    if i == 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            pr.remove(i)
            break
if len(pr) == 0:
    print(-1)
else:
    print(sum(pr))
    print(min(pr))
