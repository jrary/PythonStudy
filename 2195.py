import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()
P_split = []

# copy 함수를 통한 결과물을 모두 미리 가져온다
# S를 split하여 copy 함수 안에 문자열의 길이별로 저장한다
copy = [[] for _ in range(len(S)+1)]
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        copy[j-i].append(S[i:j])

def frag(p):
    print("hi")

res = 0
if len(S) < len(P):
    for i in range(len(P)):
        for j in range(i, len(P)):
            P_split.append(P[i:j])
else:
    P_split = P

print(P_split)


print(res)
