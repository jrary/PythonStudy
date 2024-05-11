import sys

vowel = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, sys.stdin.readline().split())
words = list(sys.stdin.readline().split())

words.sort() 

def check(arr):
    v_count, c_count = 0, 0 # 모음 개수, 자음 개수

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def backtracking(word):

    if len(word) == L:
        if check(word):
            print("".join(word))
            return

    for i in range(len(word), C):
        if word[-1] < words[i]:
            word.append(words[i])
            backtracking(word)
            word.pop()

for i in range(C - L + 1):
    a = [words[i]]
    backtracking(a)