# https://velog.io/@younghoondoodoom/%EB%B0%B1%EC%A4%80-11729-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C
def hanoi(n, start, end, to):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, to, end)
        print(start, to)
        hanoi(n-1, end, start, to)


n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)
