import sys
t, m = map(int, sys.stdin.readline().split())
m -= 45
if m < 0:
    m += 60
    t -= 1
    if t < 0:
        t += 24
print(t, m)
