
T = int(input())

for test_case in range(1, T + 1):
    arr=list(map(int,input().split()))
    result=0
    for num in arr:
        if num%2!=0:
            result+=num
    print(f'#{test_case} {result}')