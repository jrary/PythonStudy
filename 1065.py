import sys
n = int(sys.stdin.readline())
res = 0
for i in range(n):
    j = i+1
    if j == 1000:
        continue
    elif j >= 100:
        a = []
        while j/10 != 0:
            a.append(j % 10)
            j //= 10
        if (a[0]-a[1]) == (a[1]-a[2]):
            res += 1
    else:
        res += 1
print(res)
