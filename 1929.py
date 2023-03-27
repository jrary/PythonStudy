import sys
m, n = map(int, sys.stdin.readline().split())
for i in range(m, n+1):
    if i == 1:
        continue
    isDec = True
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            isDec = False
            break
    if isDec:
        print(i)
