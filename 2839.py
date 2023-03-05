import sys
n = int(sys.stdin.readline())

for i in range(n//5, -2, -1):
    if i == -1:
        print(-1)
        break
    j = (n-i*5) / 3
    if j % 1 == 0:
        print(int(i+j))
        break
