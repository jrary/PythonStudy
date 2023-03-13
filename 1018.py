import sys
m, n = map(int, sys.stdin.readline().split())
a = []
for i in range(m):
    a.append(list(sys.stdin.readline().strip()))
# 올바른 체스판 만들기
chess = [[_ for _ in range(0)] for _ in range(2)]
for i in range(8):
    temp_1 = []
    temp_2 = []
    for j in range(8):
        temp_1.append('W' if (i+j) % 2 == 0 else 'B')
        temp_2.append('W' if (i+j) % 2 != 0 else 'B')
    chess[0].append(list(temp_1))
    chess[1].append(list(temp_2))
# 올바른 체스판과 현재 체스판 전부 비교
count_min = 64
for i in range(0, m-7):
    for j in range(0, n-7):
        for k in range(2):
            count = 0
            for p in range(8):
                for q in range(8):
                    if a[i+p][j+q] != chess[k][p][q]:
                        count += 1
            if count < count_min:
                count_min = count
print(count_min)
