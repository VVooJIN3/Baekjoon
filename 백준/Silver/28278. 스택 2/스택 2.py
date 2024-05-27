import sys
input=sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    line = input()
    if line[0] == '1':
        num = int(line[2:])
        stack.append(num)
    elif line[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif line[0] == '3':
        print(len(stack))
    elif line[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif line[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
