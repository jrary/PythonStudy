import sys
n = int(sys.stdin.readline())


def getRoom(a):
    if a == 1:
        return 1
    else:
        a -= 1
        temp = 1
        while a > 0:
            a -= (temp*6)
            temp += 1
        return temp


print(getRoom(n))
