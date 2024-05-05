T = int(input())

for test_case in range(1, T + 1):
    bit=input()
    recover_bit=list(0 for _ in range(len(bit)))
    count=0
    for i in range(len(bit)):
        if int(bit[i]) == recover_bit[i]:
            continue
        else:
            count+=1
            for j in range(i,len(bit)):
                recover_bit[j]=int(bit[i])
    print(f'#{test_case} {count}')