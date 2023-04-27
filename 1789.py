import sys
N = int(sys.stdin.readline())
t = 0
for i in range(N):
    sum = i*(i+1)/2
    if sum > N:
        t = i-1
        break
print(t)
