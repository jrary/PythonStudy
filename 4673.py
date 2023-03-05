n = list(range(1, 10001))
for i in range(1, 10001):
    m = []
    temp = i
    s = i
    while temp != 0:
        s += temp % 10
        temp //= 10
    if s in n:
        n.remove(s)
for i in n:
    print(i)
