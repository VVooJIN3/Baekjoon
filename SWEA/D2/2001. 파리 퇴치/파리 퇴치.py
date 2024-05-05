T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr=[]
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    
    max_kill=0
    for x in range(N-M+1):
        for y in range(N-M+1):
            #kill_count=sum(arr[x:x+M-1][y],arr[x][y:y+M-1])
            kill_count = sum(sum(arr[i][y:y+M]) for i in range(x, x+M))
            if max_kill<kill_count:
                max_kill=kill_count

    print(f'#{test_case} {max_kill}')    