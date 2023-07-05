import sys
res = []
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break

    if a == b and b == c:
        res.append('Equilateral')
    elif a == b or b == c or a == c:
        res.append('Isosceles')
    else:
        res.append('Scalene')
for r in res:
    print(r)