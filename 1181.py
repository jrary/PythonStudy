n = int(input())
x = []

for i in range(n):
    x.append(input())

a = list(set(x))
b = sorted(a)
b.sort(key=len)

for i in b:
    print(i)
