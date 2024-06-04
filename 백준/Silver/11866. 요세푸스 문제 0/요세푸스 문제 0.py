from collections import deque
N, K = map(int,input().split())
arr=list(i for i in range(1,N+1))
queue=deque(arr)
temp=[]
result=[]
while queue:
    # K-1번 앞에서 빼서 뒤로 다시 넣음
    queue.rotate(-(K-1))
    # K번째 사람을 빼서 result에 추가
    result.append(queue.popleft())

#결과출력
print('<', ', '.join(map(str, result)),'>', sep='')
