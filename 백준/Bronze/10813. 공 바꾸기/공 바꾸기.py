#바구니 수 N, 공을 바꿀 횟수 M
import sys

N, M = map(int,input().split())
basket=[i for i in range(1,N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    basket[a-1],basket[b-1] = basket[b-1],basket[a-1]

print(*basket)