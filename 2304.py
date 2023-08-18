import sys

N = int(sys.stdin.readline())
P = []
top = 0
for _ in range(N):
    P.append(list(map(int, sys.stdin.readline().split())))
    if P[-1][1] > top:
        top = P[-1][1]

P.sort()
h = 0
w = 0
res = 0
for p, l in P:
    if l > h:
        res += h * (p-w)
        w, h = p, l
        
h = 0
w = P[-1][0]
for p, l in reversed(P):
    if l > h:
        res += h * (w-p)
        w, h = p, l

top_list = []
for p, l in P:
    if l == top:
        top_list.append(p)
top_list.sort()
res += top * (max(top_list) - min(top_list) + 1)

print(res)    