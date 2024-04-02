import sys

X, Y, W, S = map(int, sys.stdin.readline().split())

if W * 2 <= S:
    # 블록을 두 번 이동하는 것이 대각선으로 가는 것보다 빠른 경우
    # 전부 직선으로 걸어야 함
    print((X + Y) * W)
elif S < W:
    # 블록을 한 번 이동하는 것이 대각선으로 가는 것보다 느린 경우
    # 전부 대각선으로 움직여야 함
    if (X + Y) % 2 == 0:
        print(max(X, Y) * S)
    else:
        print((max(X, Y) - 1) * S + W)
else:
    # 최대한 대각선으로 진행, 나머지는 거리로 움직임
    print(min(X, Y) * S + (abs(X - Y) * W))