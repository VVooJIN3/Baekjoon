N, M = map(int,input().split())
values=[0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int,input().split())
    for n in range(i-1,j):
        values[n]=k
print(*values)