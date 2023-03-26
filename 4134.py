import sys
n = int(sys.stdin.readline())
tc = []
for _ in range(n):
    tc.append(int(sys.stdin.readline()))
for i in tc:
    if i == 0 or i == 1:
        print(2)
        continue
    j = i
    while True:
        isDec = True
        for m in range(2, int(j**(1/2))+1):
            if j % m == 0:
                isDec = False
                break
        if isDec:
            print(j)
            break
        j += 1
