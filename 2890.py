import sys
R, C = map(int, sys.stdin.readline().split())
pic = []
for _ in range(R):
    pic.append(sys.stdin.readline().strip())

now_rank = 0
now_in = 0
rank = {}
for i in range(C-2, 0, -1):
    for j in range(R):
        if pic[j][i] != ".":
            if pic[j][i] in rank:
                continue
            if i != now_in:
                now_in = i
                now_rank += 1

            rank[pic[j][i]] = now_rank

keys = sorted(rank.keys())
for i in keys:
    print(rank[i])
