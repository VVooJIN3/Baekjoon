import sys
N, M = map(int,input().split())
basket=[i for i in range(1,N+1)]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    basket=basket[:i-1]+basket[i-1:j][::-1]+basket[j:]

print(*basket)
    