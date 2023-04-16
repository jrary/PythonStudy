import sys
n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))
rope.sort()
max = 0
for i in range(n):
    m = rope[i]*(n-i)
    if max < m:
        max = m
print(max)
