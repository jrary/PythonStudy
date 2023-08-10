import sys
N, P = map(str, sys.stdin.readline().split())
N = int(N)
if P == 'Y':
    P = 1
elif P == 'F':
    P = 2
elif P == 'O':
    P = 3

member = set()
for _ in range(N):
    member.add(sys.stdin.readline().strip())

print(len(member)//P)