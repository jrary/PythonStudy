import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
max_sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = card[i]+card[j]+card[k]
            if s > max_sum and s <= m:
                max_sum = s
print(max_sum)
