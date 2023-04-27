import sys
li = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
n = 0
i = 0
while i < len(li):
    if li[i:i+len(word)] == word:
        n += 1
        i += len(word)
    else:
        i += 1
print(n)
