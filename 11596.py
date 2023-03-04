import sys
n1 = list(map(int, sys.stdin.readline().split()))
n2 = list(map(int, sys.stdin.readline().split()))
n1.sort()
n2.sort()
if n1 == n2:
    if n1[0]**2+n1[1]**2 == n1[2]**2:
        print('YES')
    else:
        print()
        print('NO')
else:
    print('NO')
