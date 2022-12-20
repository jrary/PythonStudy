n = int(input())
x = []
y = []
z = []


# Get 2 dimension list
for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(n):
    y.append(x[i][0])
    z.append(x[i][1])

b = sorted(y)
c = sorted(z)

for i in range(n):
    print(b[i], c[i])
