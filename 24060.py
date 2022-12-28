def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global N, R
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i = i+1
        else:
            tmp.append(A[j])
            j = j+1
    while i <= q:
        tmp.append(A[i])
        i = i+1
    while j <= r:
        tmp.append(A[j])
        j = j+1
    i = p
    for a in tmp:
        A[i] = a
        N = N+1
        if N == k:
            R = a
        i = i+1


A = []
N, R = 0, 0
n, k = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(A, 0, n-1)

if R == 0:
    print(-1)
else:
    print(R)
