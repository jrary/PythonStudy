n = int(input())
x = []

for i in range(n):
    x.append(list(map(int, input().split())))

y = sorted(x)

for i in range(n):
    print(y[i][0], y[i][1])
