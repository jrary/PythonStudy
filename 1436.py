import sys
n = int(sys.stdin.readline())
i = 0
res = 0
while n != res:
    i = i+1
    temp = i
    while temp >= 666:
        if temp % 1000 == 666:
            res = res+1
            break
        else:
            temp = temp//10
print(i)
