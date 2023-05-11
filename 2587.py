import sys
N = []
for _ in range(5):
    N.append(int(sys.stdin.readline()))
N.sort()
print(int(sum(N)/5))
print(N[2])
