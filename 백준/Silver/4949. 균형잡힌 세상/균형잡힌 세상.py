import sys
input = sys.stdin.readline

while True:
    stack = []
    line = input().rstrip()  # 오른쪽 개행 문자를 제거하기 위해 rstrip() 사용
    result = 'yes'
    if line == '.':
        break
    for i in range(len(line)):
        if line[i] in ['[', '(']:
            stack.append(line[i])
        elif line[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break
        elif line[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)
