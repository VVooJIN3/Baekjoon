#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액
#을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 
#영수증에 적힌 총 금액과 일치하는지 검사해보자.

X=int(input())
N=int(input())
sum=0
for i in range(1,N+1):
    a, b=map(int,input().split())
    sum+=a*b

result='Yes' if X==sum else 'No'

print(result)