import sys
num = []
while True:
    t = int(sys.stdin.readline())
    if t == 0:
        break
    num.append(t)
for n in num:
    count = 2*n-n
    for i in range(n+1, 2*n+1):
        if i == 1:
            continue
        isDec = True
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                count -= 1
                break
    print(count)
