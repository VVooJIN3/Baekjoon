import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    line = input()
    result = 'YES'
    for i in range(len(line)):
        if line[i] == '(':
            stack.append('(')
        elif line[i] == ')':
            if stack:
                stack.pop()
            else:
                result='NO'
                break
    if stack:
        result = 'NO'
    print(result)
