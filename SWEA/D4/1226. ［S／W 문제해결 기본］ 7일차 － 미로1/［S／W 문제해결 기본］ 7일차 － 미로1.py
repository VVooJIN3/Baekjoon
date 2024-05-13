for test_case in range(1, 11):
    N=int(input())
    maze=[]
    for i in range(16):
        maze.append(list(input()))
    result=0
    def dfs(x,y):
        global result
        #목적지에 도달한 경우
        if maze[x][y]=='3':
            result=1
        #벽(1)에 도달한 경우 돌아가기
        if maze[x][y]=='1':
            return
        if maze[x][y]=='0':
            maze[x][y]='1'
        #오른쪽,아래,왼쪽,위 순으로 진행
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
    dfs(1,1)
    print(f'#{test_case} {result}')