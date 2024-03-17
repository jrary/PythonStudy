import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

# copy 함수를 통한 결과물을 모두 미리 가져온다
# S를 split하여 copy 함수 안에 문자열의 길이별로 저장한다
copy = [[] for _ in range(len(S)+1)]
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        copy[j-i].append(S[i:j])

# 가장 긴 특정 문자열이 매칭됐다면 해당 문자열을 제외한 앞, 뒤 문자열에 대하여 다시 매칭을 진행
res = 0
def frag(p):
    global res
    if len(p) <= 1:
        res += 1
        return
    for i in range(len(S), 1, -1):
        for key in copy[i]:
            if key in p:
                idx = p.find(key)
                res += 1
                frag(p[:idx])
                frag(p[idx+i:])
                return          

frag(P)
print(res)