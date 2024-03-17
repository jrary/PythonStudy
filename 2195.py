import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

res = 0
idx = 0

while idx < len(P):
    copy = ''
    # S에서 P의 인덱스 이후 나머지를 찾았다면
    if S.find(P[idx:]) != -1:
        res += 1
        break
    # P의 길이로 반복문
    for j in range(idx, len(P)):
        copy += P[j]
        if S.find(copy) == -1:
            res += 1
            idx = j
            break

print(res)