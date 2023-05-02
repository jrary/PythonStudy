import sys
w = sys.stdin.readline().strip()
f = 1
for i in range(int(len(w))):
    if w[i] != w[len(w)-1-i]:
        f = 0
        break
print(f)
