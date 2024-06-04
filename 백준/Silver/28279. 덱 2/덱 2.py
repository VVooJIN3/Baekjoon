from collections import deque
import sys
input=sys.stdin.readline
N = int(input())
deq = deque()

for _ in range(N):
    order = input()
    if order[0] in ('1', '2'):
        X = int(order[2:])
        deq.appendleft(X) if order[0]=='1' else deq.append(X)
    elif order[0] == '3':
        print(deq.popleft()) if deq else print(-1)
    elif order[0] == '4':
        print(deq.pop()) if deq else print(-1)
    elif order[0] == '5':
        print(len(deq))
    elif order[0] == '6':
        print(0) if deq else print(1)
    elif order[0] == '7':
        print(deq[0]) if deq else print(-1)
    elif order[0] == '8':
        print(deq[-1]) if deq else print(-1)

