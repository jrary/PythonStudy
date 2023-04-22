import sys
T = int(sys.stdin.readline())
N = []
for _ in range(T):
    N.append(int(sys.stdin.readline()))

z = [1, 0]
o = [0, 1]


for i in range(2, 41):
    z.append(z[i-1]+z[i-2])
    o.append(o[i-1]+o[i-2])


for i in N:
    print(z[i], o[i])
