N, M = map(int,input().split())

A=[]
B=[]
#결과행렬 초기화
result=[[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        result[i][j]=A[i][j]+B[i][j]

for row in result:
    print(*row)