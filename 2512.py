import sys
N = int(sys.stdin.readline())
R = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

limit_max = max(R)
limit_min = 1

while limit_max >= limit_min:
    mid = (limit_max+limit_min) // 2
    limit_money = 0
    for r in R:
        if mid < r:
            limit_money += mid
        else:
            limit_money += r
    if limit_money > M:
        limit_max = mid - 1
    else:
        limit_min = mid + 1

print(limit_max)