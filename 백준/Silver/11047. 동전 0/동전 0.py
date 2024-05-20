N, K = map(int,input().split())

coins=[]
for _ in range(N):
    coin=int(input())
    if coin <= K:
        coins.append(coin)
count=0
i=len(coins)-1
while K!=0:
    if coins[i]<=K:
        count+=K//coins[i]
        K=K%coins[i]
    i-=1
print(count)
