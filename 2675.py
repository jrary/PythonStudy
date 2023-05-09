import sys
N = int(sys.stdin.readline())
for _ in range(N):
    num, li = map(str, sys.stdin.readline().strip().split())
    num = int(num)
    res = ''
    for c in li:
        res += c*num
    print(res)
