import sys
n = int(sys.stdin.readline())
tree = []
diff = []
for i in range(n):
    tree.append(int(sys.stdin.readline()))
tree.sort()
# 나무 간의 간격 구하기
for i in range(1, n):
    diff.append(tree[i]-tree[i-1])
# 간격들의 최대공약수 구하기
a = diff[0]
b = diff[1]
for i in range(1, n-1):
    b = diff[i]
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
# 각 간격에서 최대공배수를 나눈 몫보다 1 작은 나무씩 심는다
res = 0
for i in range(n-1):
    res += (diff[i]//a)-1
print(res)
