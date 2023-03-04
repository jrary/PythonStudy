import sys
n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
res = 0
for i in range(3):
    ans = n1*(n2 % 10)
    print(ans)
    res += ans*(10**i)
    n2 //= 10
print(res)
