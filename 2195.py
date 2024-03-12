import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()
P_split = []
copy = [[] for _ in range(len(S)+1)]
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        copy[j-i].append(S[i:j])

def frag(p):
    

res = 0
while len(P_split) > 0:
    for i in range(len(P)):
        for j in range(i, len(P)):
            


print(res)
