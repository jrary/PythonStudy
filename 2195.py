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
res = 0
def frag(p):
    global res
    if len(p) <= 1:
        res += 1
        #print(p)
        return
    for i in range(len(S), 1, -1):
        for key in copy[i]:
            if key in p:
                idx = p.find(key)
                #print(key,":", p, "->", p[:idx], "+", p[idx+i:])
                res += 1
                frag(p[:idx])
                frag(p[idx+i:])
                return          

frag(P)
# print(copy)
print(res)
