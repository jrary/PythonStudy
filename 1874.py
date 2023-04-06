import sys
n = int(sys.stdin.readline())
li = []
stack = [0]
res = []
push = 0
for _ in range(n):
    li.append(int(sys.stdin.readline()))
# 입력 배열의 몇 번째 숫자를 추가 중인지
for i in li:
    # 스택에 해당 숫자가 있을 경우 - pop
    if stack[-1] == i:
        stack.pop()
        res.append('-')
        continue
    # push
    else:
        while True:
            push += 1
            # 끝까지 push를 진행해도 답이 나오지 않은 경우. 불가능
            if push > n:
                res = [-1]
                break
            if push == i:
                res.append('+')
                res.append('-')
                break
            else:
                res.append('+')
                stack.append(push)

if -1 in res:
    print('NO')
else:
    for i in res:
        print(i)
