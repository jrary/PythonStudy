import sys
sentence = []
# 입력받기
# ' .'과 같은 문자열의 경우, strip() 사용 시 첫 번째 공백이 없어지므로,
# 종료조건 온점을 판별하기 위해 strip 이전의 문자열 길이를 비교하는 과정도 거친다
while True:
    s = sys.stdin.readline()
    if len(s) <= 2 and s.strip() == '.':
        break
    sentence.append(s.strip())

for i in sentence:
    open = [0]
    for w in i:
        # 왼쪽 괄호 발견 시 'open' 리스트에 추가
        if w == '(' or w == '[':
            open.append(w)
        # 오른쪽 괄호 발견 시, 맞는 괄호가 마지막에 있으면 'open' 리스트에서 해당 괄호 제거
        elif w == ')' and open[-1] == '(':
            open.pop()
        elif w == ']' and open[-1] == '[':
            open.pop()
        elif w == ')' or w == ']':
            open.append(-1)

    if open[-1] == 0:
        print('yes')
    else:
        print('no')
