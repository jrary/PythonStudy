import sys
N = int(sys.stdin.readline())
t = 1
for i in range(N+1):
    sum = i*(i+1)/2
    if sum > N:
        t = i - 1
        break
print(t)
