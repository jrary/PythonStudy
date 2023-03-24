import sys
a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

a = a1*b2+a2*b1
b = b1*b2

m, n = a, b
while n != 0:
    temp = n
    n = m % n
    m = temp
a = a//m
b = b//m
print(a, b)
