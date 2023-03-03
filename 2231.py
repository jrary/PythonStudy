import sys
n = int(sys.stdin.readline())
res = 0
for i in range(n):
    m = i
    temp = i
    while temp != 0:
        m += temp % 10
        temp //= 10
    if m == n:
        res = i
        break
print(res)
