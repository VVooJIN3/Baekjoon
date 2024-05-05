T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    s=set()
    count=0
    while len(s)!=10:
        count+=1
        str_N=str(count*N)
        for i in range(len(str_N)):
            if str_N[i] not in s:
                s.add(str_N[i])
    print(f'#{test_case} {str_N}')