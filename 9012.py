import sys
n = int(sys.stdin.readline())
br = []
for _ in range(n):
    br.append(sys.stdin.readline().strip())


def stack(line):
    s = []
    for c in line:
        if c == '(':
            s.append(c)
        elif c == ')':
            if len(s) == 0:
                return (False)
            else:
                s.pop()
    if len(s) == 0:
        return (True)
    else:
        return (False)


for li in br:
    if stack(li):
        print('YES')
    else:
        print('NO')
