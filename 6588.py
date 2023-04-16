import sys
li = []
while True:
    t = int(sys.stdin.readline())
    if t == 0:
        break
    li.append(t)
m = max(li)
dec = [True for i in range(m+1)]
dec[0], dec[1] = False, False
for i in range(2, m+1):
    if dec[i]:
        for j in range(i*2, m + 1, i):
            dec[j] = False

for i in li:
    for d in range(3, m-2):
        if dec[d] and dec[i-d]:
            print(i, '=', d, '+', i-d)
            break
    if d == m:
        print('Goldbach\'s conjecture is wrong.')
