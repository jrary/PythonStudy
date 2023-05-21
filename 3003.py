import sys
chess = [1, 1, 2, 2, 2, 8]
white = list(map(int, sys.stdin.readline().split()))
for i in range(6):
    print(chess[i]-white[i], end=' ')