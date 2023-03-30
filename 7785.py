import sys
n = int(sys.stdin.readline())
company = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b == 'enter':
        company.append(a)
    elif b == 'leave':
        company.remove(a)

company.sort(reverse=True)
for i in company:
    print(i)
