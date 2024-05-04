#(0,0) (0,1),(0,2) 
#                 (1,2)(2,2)
#                            (2,1),(2,0)
#                                        (1,0),
#                                                (1,1)
#y증가
#x증가
#y감소
#x감소 
#반복

def draw(arr,brush,status,x,y,n):
    if brush > n**2:
      return arr
    #y증가
    if status % 4==1:
        for i in range(0,n):
            if arr[x][i]==0:
                arr[x][i]=brush
                y=i
                brush+=1
        return draw(arr,brush,status+1,x,y,n)
    #x증가
    if status % 4 ==2:
        for i in range(0,n):
            if arr[i][y]==0:
                arr[i][y]=brush
                x=i
                brush+=1
        return draw(arr,brush,status+1,x,y,n)
     #y감소
    if status % 4==3:
        for i in range(n-1,-1,-1):
            if arr[x][i]==0:
                arr[x][i]=brush
                y=i
                brush+=1
        return draw(arr,brush,status+1,x,y,n)
    #x감소
    if status % 4==0:
        for i in range(n-1,-1,-1):
            if arr[i][y]==0:
                arr[i][y]=brush
                x=i
                brush+=1
        return draw(arr,brush,status+1,x,y,n)

        
        
T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    brush=1
    status=1
    #달팽이 껍질 초기화
    shell=[[0 for _ in range(n)] for _ in range(n)]
    result=draw(shell,brush,status,0,0,n)
    print(f'#{test_case}')
    for element in result:
        print(*element)