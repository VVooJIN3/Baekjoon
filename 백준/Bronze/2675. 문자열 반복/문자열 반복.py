import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    result=''
    R, S=input().split()
    R=int(R)
    
    for i in S:
        result+=i*R
    print(result)
    
    