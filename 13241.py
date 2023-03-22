import sys
a, b = map(int, sys.stdin.readline().split())
m, n = a, b
if a < b:
    m, n = b, a
while n != 0:
    temp = n
    n = m % n
    m = temp
print(int((a/m)*(b/m)*m))
