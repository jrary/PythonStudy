import sys
N = int(sys.stdin.readline())
for _ in range(N):
    price = int(sys.stdin.readline())
    coin = [25, 10, 5, 1]
    ret = [0, 0, 0, 0]
    for i in range(4):
        c = coin[i]
        while price >= c:
            ret[i] += 1
            price -= c
    print(ret[0], ret[1], ret[2], ret[3])
