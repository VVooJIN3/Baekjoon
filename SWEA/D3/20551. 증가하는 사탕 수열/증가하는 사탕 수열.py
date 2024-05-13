T = int(input())

for test_case in range(1, T + 1):
    A, B, C=map(int,input().split())
    eat=0
    while A>=B or B>=C:
        if B>=C:
            B-=1
            eat+=1
        if A>=B:
            A-=1
            eat+=1
        if A==0 or B==0:
            eat=-1
            break
    print(f'#{test_case} {eat}')
          