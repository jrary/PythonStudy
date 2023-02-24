import sys
n = int(sys.stdin.readline())
a = []
while n/10 != 0:
    a.append(n % 10)
    n //= 10
a.sort()
for i in range(len(a)-1, -1, -1):
    print(a[i], end='')
