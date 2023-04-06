import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


def cut_tree(start, end):
    h = start+(end-start)//2
    cut_len = 0
    big_tree = 0
    # 잘라보기
    for i in tree:
        # 절단기의 높이보다 나무의 높이가 더 크다 - 자를 수 있는 경우
        if i-h > 0:
            big_tree += 1
            cut_len += i-h
    # 절단기가 높을 때
    if cut_len < m:
        return cut_tree(start, h)
    # 정확하게 잘랐을 때
    elif cut_len == m:
        return h
    # 절단기가 낮을 때
    else:
        # 만약 1m를 높혔을 때, 잘라야 하는 최소 길이가 나오지 않을 경우,
        # 현재 위치가 최적 결과가 된다
        if cut_len-big_tree < m:
            return h
        else:
            return cut_tree(h, end)


print(cut_tree(0, max(tree)))
