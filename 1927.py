import sys
n = int(sys.stdin.readline())
heap = []
pt = []
for _ in range(n):
    t = int(sys.stdin.readline())
    if t == 0:
        if len(heap) == 0:
            pt.append(0)
        else:
            pt.append(heap[0])
            heap.remove(heap[0])
    else:
        heap.append(t)
        i = len(heap) - 1
        while heap[i//2] > heap[i]:
            heap[i//2], heap[i] = heap[i], heap[i//2]
            i //= 2
    print(heap)
for i in pt:
    print(i)
