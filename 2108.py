import sys


def mode(a):
    # Tuple로 개수 세기
    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    # Max값 찾고, max인 수 모아서 list r에 저장하기
    m = 0
    r = []
    for j in cnt:
        if cnt[j] > m:
            m = cnt[j]
            r = []
            r.append(j)
        elif cnt[j] == m:
            r.append(j)
    # 최빈값이 1개라면, 그것을 리턴 / 2개 이상이면 두 번째로 작은 값 리턴
    if len(r) == 1:
        return r[0]
    else:
        r.sort()
        return r[1]


n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
print(round(sum(a)/n))
print(a[n//2])
print(mode(a))
print(max(a)-min(a))
