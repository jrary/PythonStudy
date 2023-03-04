import sys
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
res = 0
wait = 0
for i in range(n):
    wait += time[i]
    res += wait
print(res)
