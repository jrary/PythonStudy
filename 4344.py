import sys
N = int(sys.stdin.readline())
for _ in range(N):
    l =[]
    l = list(map(int, sys.stdin.readline().split()))
    key = l[0]
    score = l[1:]
    
    count = 0
    avg = sum(score)/key
    for c in score:
        if c>avg:
            count+=1

    print('{:.3f}%'.format(count/key*100, 3))