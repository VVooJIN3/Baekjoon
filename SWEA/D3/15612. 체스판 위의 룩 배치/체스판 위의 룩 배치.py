
T = int(input())
for test_case in range(1, T + 1):
    arr = []
    rook_x=[]
    rook_y=[]
    result='yes'
    rook_count=0
    for i in range(8):
        line = input()
        while 'O' in line:
            rook_index = line.index('O')
            rook_x.append(i)
            rook_y.append(rook_index)
            rook_count+=1
            line = line.replace('O', '.', 1)
    if len(rook_x) != len(set(rook_x)) or len(rook_y) != len(set(rook_y)) or rook_count!=8:
        result='no'
    
    print(f'#{test_case} {result}')

