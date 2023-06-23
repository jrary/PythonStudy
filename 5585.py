import sys
n = int(sys.stdin.readline())
N = 1000 - n
count = 0
coin = [500, 100, 50, 10, 5, 1]
for c in coin:
    while N >= c:
        N -= c
        count+=1
print(count)