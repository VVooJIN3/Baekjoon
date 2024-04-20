#N의 약수 중 K번째로 작은 수 출력하기
N,K=map(int,input().split())
arr=[]
i=0
while K!=0:
    i+=1
    #i로 나눠질 때 K를 1씩 차감시키고, K가 0이될 때 
    if N%i==0:
        K-=1
    #K번 째 약수가 존재하지 않을 때(i가 N보다 커질 때까지 while문이 반복될 때)
    #반복문을 종료하고 0 출력
    if i>N:
        i=0
        break
print(i)
        