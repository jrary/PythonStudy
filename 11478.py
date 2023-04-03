import sys
sentence = sys.stdin.readline().strip()
sub_sentence = []
for i in range(1, len(sentence)+1):  # 자를 문자열의 길이
    for j in range(len(sentence)-i+1):  # 자를 부분
        sub_sentence.append(sentence[j:j+i])
sub_sentence = set(sub_sentence)  # 중복 제거
print(len(sub_sentence))
