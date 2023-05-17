import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
B += C
while B >= 60:
    B -= 60
    A += 1
while A >= 24:
    A -= 24
print(A, B)
