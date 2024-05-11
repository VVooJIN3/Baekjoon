for test_case in range(1, 11):    
    N=int(input())
    arr=[]
    count=0
    
    for _ in range(8):
        arr.append(list(input()))
        
    for i in range(0,8):
        for j in range(0,8-N+1):
            s=''.join(arr[i][j:j+N])
            reversed_s=s[::-1]
            if s==reversed_s:
                count+=1
    for i in range(0,8):
        for j in range(0,8-N+1):
            s=''.join(arr[j+k][i] for k in range(N))
            reversed_s=s[::-1]
            if s==reversed_s:
                count+=1
    print(f'#{test_case} {count}')