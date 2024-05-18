def draw(i,line,arr):
    line.append(1)
    for j in range(1,i):
        line.append(arr[i-1][j-1]+arr[i-1][j])
    line.append(1)
    return line
T = int(input())

for test_case in range(1, T + 1):
    arr=[[1],[1,1]]
    N=int(input())
    for i in range(2,N):
        arr.append(draw(i,[],arr))
    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])
                   
        
        