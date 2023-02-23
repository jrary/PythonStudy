import sys
n = []
n = list(map(int, sys.stdin.readline().split()))
x = set()
for i in range(n[0]):
    x.add(sys.stdin.readline().strip())
res = 0
for i in range(n[1]):
    y = sys.stdin.readline().strip()
    if y in x:
        res += 1
print(res)
