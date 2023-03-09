import sys
n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
count = 0
for i in m:
    isDec = True
    if i == 1:
        isDec = False
        continue
    if i == 2:
        count += 1
        continue
    for j in range(2, i):
        if i % j == 0:
            isDec = False
            break
    if isDec:
        count += 1
print(count)
