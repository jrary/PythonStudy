import sys
a, b = map(int, sys.stdin.readline().split())
m = min(a, b)
n = max(a, b)
print(int((m+n)*(n-m+1)/2))
