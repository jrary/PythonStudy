import sys

T = int(sys.stdin.readline())
N = []
for _ in range(T):
    N.append(int(sys.stdin.readline()))

seq = [0]

for i in range(1, max(N)+1):
    if i == 1 or i == 2 :
        seq.append(1)
    else:
        seq.append(seq[i - 3] + seq[i - 2])

for i in range(T):
    print(seq[N[i]])