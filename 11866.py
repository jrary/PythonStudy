import sys
    
N, K = map(int, sys.stdin.readline().split())
table = list(range(1, N+1))
stack = []
pos = 0

while len(table) != 0:
    pos += K-1
    pos %= len(table)
    stack.append(table[pos])
    del table[pos]

print("<" + ", ".join(map(str, stack)) + ">")