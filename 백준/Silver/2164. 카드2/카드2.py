import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
queue=deque(range(1,N+1))
while len(queue) > 1:
    #1. 맨위 카드를 버림
    queue.popleft()

    #2. 다음 맨위 카드를 마지막 순서로 이동
    queue.append(queue.popleft())
print(queue[0])
