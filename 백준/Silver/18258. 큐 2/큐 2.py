from collections import deque
import sys

input = sys.stdin.readline

queue = deque()
N = int(input())
for _ in range(N):
    line = input()
    if 'push' in line:
        order, num = line.split()
        queue.append(int(num))
    elif 'front' in line:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in line:
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif 'empty' in line:
        print(0) if queue else print(1)
    elif 'size' in line:
        print(len(queue))
    elif 'pop' in line:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
