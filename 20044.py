import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
team = []
for i in range(n):
    team.append(li[i]+li[2*n-i-1])
print(min(team))
