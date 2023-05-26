import sys
N = int(sys.stdin.readline())

a = 2
for i in range(N):
    a += a-1

print(a**2)