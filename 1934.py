import sys
n = int(sys.stdin.readline())
T = []
for _ in range(n):
    T.append(list(map(int, sys.stdin.readline().split())))


def gcd(a, b):
    if a > b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


for i, j in T:
    g = gcd(i, j)
    print(int(g*(i/g)*(j/g)))
