import sys
p = sys.stdin.readline().strip()
exp = []
# 이전 문자가 기호이면 0, 숫자이면 1
prev = 0
for i in p:
    if i.isdigit():
        if prev == 0:
            exp.append(int(i))
        else:
            exp[-1] = exp[-1]*10+int(i)
        prev = 1
    else:
        exp.append(i)
        prev = 0
res = 0
# - 기호 이후이면 1, 이전이면 0
mi = 0
for i in exp:
    if i == '-':
        mi = 1
    elif i == '+':
        continue
    else:
        if mi == 0:
            res += i
        else:
            res -= i
print(res)
