T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))
    result=0
    def dfs(count,number):
        global result
        if number == K:
            result+=1
            return
        #모든 숫자를 사용한 경우
        if count==N:
            return
        dfs(count+1,number+arr[count])
        #되돌아온경우
        dfs(count+1,number)
    
    dfs(0,0)
    print(f'#{test_case} {result}')
    
    