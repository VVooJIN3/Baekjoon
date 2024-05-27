import sys
input=sys.stdin.readline

stack=[]
K=int(input())
for _ in range(K):
    line=int(input())
    if line:
        stack.append(line)
    else:
        stack.pop()
print(sum(stack))