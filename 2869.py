import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
day = math.ceil((v - b)/(a-b))
print(day)
