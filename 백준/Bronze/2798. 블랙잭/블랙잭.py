N, M = map(int,input().split())
cards=list(map(int,input().split()))
max_value=0
cards=sorted(cards, reverse=True)
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            value=cards[i]+cards[j]+cards[k]
            if M < value:
              continue
            if max_value <value:
                max_value = value
print(max_value)