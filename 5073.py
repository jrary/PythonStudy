import sys
res = []
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b :
        a, b = b, a

    if c >= a + b:
        res.append('Invalid')
    elif a == b and b == c:
        res.append('Equilateral')
    elif a == b or b == c:
        res.append('Isosceles')
    else:
        res.append('Scalene')
for r in res:
    print(r)