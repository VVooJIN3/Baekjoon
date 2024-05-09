def iterative(farm,i,N):
    index=int((N-1)/2)
    result=farm[i][index]
    if i<=index:    
        for num in range(1,i+1,+1):
            result+=farm[i][index+num]
            result+=farm[i][index-num]
    elif i>index:
        for num in range(N-1-i,0,-1):
            
            result+=farm[i][index+num]
            result+=farm[i][index-num]
    return result

T = int(input())
for test_case in range(1, T + 1):
    #농장의 크기
    N=int(input())
    farm=[]
    price=0
    #농장 내 농작물 가치 입력
    for i in range(N):
        farm.append([int(x) for x in input()])     
    #1x1크기 : (0,0)
    #3x3크기 : (0,1) / (1,0),(1,1),(1,2) / (2,1)
    #5x5크기 : (0,2) / (1,1),(1,2),(1,3) / (2,0),(2,1),(2,2),(2,3),(2,4) / (3,1),(3,2),(3,3) / (4,2)
    #...=> 공식 : (0,[N-1]/2) / (1,[[N-1]/2] -1), (1,[N-1]/2), (1,[[N-1]/2] +1)/ (2,(N-1]/2]-2) ...
    for i in range(N):
        price+=iterative(farm,i,N)
    print(f'#{test_case} {price}')
        
