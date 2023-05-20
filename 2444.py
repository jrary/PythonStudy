import sys
N = int(sys.stdin.readline())
for i in range(1, N+1):
    for _ in range(N-i):
        print(' ', end='')
    for _ in range(i*2-1):
        print('*', end='')
    print()
for i in range(N-1, 0, -1):
    for _ in range(N-i):
        print(' ', end='')
    for _ in range(i*2-1):
        print('*', end='')
    print()