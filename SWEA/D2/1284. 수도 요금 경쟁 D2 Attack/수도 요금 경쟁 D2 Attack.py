
T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int,input().split())
    #A사 : 1리터당 P원의 돈을 내야한다.
    A_fee=W*P
    #B사 : 기본요금 Q + 월간사용량 R이상인 경우, R을 초과한 리터당 S원
    if W>=R:
        B_fee=Q+(W-R)*S
    else:
        B_fee=Q
    print(f'#{test_case} {min(A_fee,B_fee)}')