import sys
dish = sys.stdin.readline().strip()
now = 0
height = 0
for d in dish:
    if d == now:
        height += 5
    else:
        now = d
        height += 10
print(height)
