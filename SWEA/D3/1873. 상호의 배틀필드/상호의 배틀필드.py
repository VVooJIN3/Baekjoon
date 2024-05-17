def is_here(line):
    tank = ''
    if '>' in line:
        tank = '>'
    if '<' in line:
        tank = '<'
    if '^' in line:
        tank = '^'
    if 'v' in line:
        tank = 'v'
    return tank

def tank_order(order, x, y, arr):
    if order != 'S':
        #   U,D,R,L
        order_direction = ['U', 'D', 'R', 'L']
        tank_direction = ['^', 'v', '>', '<']
        index = order_direction.index(order)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        nx = x + dx[index]
        ny = y + dy[index]
        #1.탱크 방향 바꾸기
        arr[x][y] = tank_direction[index]
        if nx < 0 or ny < 0 or nx == len(arr) or ny == len(arr[0]):
            return x,y
        #2. 평지일 경우 이동
        if arr[nx][ny] == '.':
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
            x, y=nx,ny;

    else:
        tank_shoot(x, y, arr[x][y], arr)
    return x, y

def tank_shoot(x, y, tank, arr):
    #   U,D,R,L
    tank_direction = ['^', 'v', '>', '<']
    index = tank_direction.index(tank)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    nx = x + dx[index]
    ny = y + dy[index]
    if nx < 0 or ny < 0 or nx == len(arr) or ny == len(arr[0]):
        return
    if arr[nx][ny] in ['.', '-']:
        tank_shoot(nx, ny, tank, arr)
    if arr[nx][ny] == '*':
        arr[nx][ny] = '.'
        return
    if arr[nx][ny] == '#':
        return
    
T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    arr = []
    for i in range(H):
        line = input()
        tank = is_here(line)
        if tank != '':
            x = i
            y = line.index(tank)
        arr.append(list(line))
    move_count = int(input())
    orders = list(input())
    for order in orders:
        x, y = tank_order(order, x, y, arr)

    print(f'#{test_case} ', end='')
    for i in range(H):
        for j in range(W):
            print(arr[i][j],end='')
        print()

