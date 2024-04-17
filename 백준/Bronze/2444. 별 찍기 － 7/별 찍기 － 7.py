N=int(input())
for i in range(N):
    print(' '*(N-1-i),end='')
    print('*'*i,end='')
    print('*',end='')
    print('*'*i)

for i in range(N-2,-1,-1):
    print(' '*(N-1-i),end='')
    print('*'*i,end='')
    print('*',end='')
    print('*'*i)