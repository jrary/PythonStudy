import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
res = 0
coin.sort(reverse=True)
for i in coin:
    while k >= i:
        k -= i
        res += 1
print(res)
