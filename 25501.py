def recursion(s, l, r, n):
    if l >= r:
        return 1, n+1
    elif s[l] != s[r]:
        return 0, n+1
    else:
        return recursion(s, l+1, r-1, n+1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)


n = int(input())
x = []

for i in range(n):
    x.append(input())


for i in x:
    a, b = isPalindrome(i)
    print(a, b)
