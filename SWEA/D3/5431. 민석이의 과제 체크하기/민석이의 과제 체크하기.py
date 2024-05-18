T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for i in range(1,N+1):
        arr.append(i)
    submit_arr = list(map(int, input().split()))
    result = []
    for i in range(N):
        if arr[i] not in submit_arr:
            result.append(arr[i])

    print(f'#{test_case} ',end='')
    print(*result)