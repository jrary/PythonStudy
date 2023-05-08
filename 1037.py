import sys
num = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
if num % 2 == 1:
    print(A[num//2]**2)
else:
    print(A[0]*A[-1])
