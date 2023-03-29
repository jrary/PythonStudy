import sys
num = int(sys.stdin.readline())
n = []
for _ in range(num):
    n.append(int(sys.stdin.readline()))
dec = []
for i in range(max(n)):
    if i == 1:
        continue
    isDec = True
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            isDec = False
            break
    if isDec:
        dec.append(i)

for m in n:
    count = 0
    for j in dec:
        t = m-j
        if t <= 0:
            continue
        if t in dec:
            if t <= j:
                count += 1
    print(count)
