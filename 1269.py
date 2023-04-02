import sys
an, bn = map(int, sys.stdin.readline().split())
res = []
for _ in range(2):
    a = list(map(int, sys.stdin.readline().split()))
    for i in a:
        res.append(i)
res_set = set(res)
print(len(res)-2*(len(res)-len(res_set)))
