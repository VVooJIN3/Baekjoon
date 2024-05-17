T = int(input())

for test_case in range(1, T + 1):
    a,b,c=map(int,input().split())
    arr=[]
    #등차수열 b-a = c-b
    #2b=a+c
    #b=(a+c)/2
    #a=2b-c
    #c=2b-a
    arr.append(abs(b-((a+c)/2)))
    arr.append(abs(a-(2*b-c)))
    arr.append(abs(c-(2*b-a)))
    print(f'#{test_case} {min(arr)}')