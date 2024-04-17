chess=[1,1,2,2,2,8]
input_piece=list(map(int,input().split()))
result=[chess[i]-input_piece[i] for i in range(len(chess))]
print(*result)
