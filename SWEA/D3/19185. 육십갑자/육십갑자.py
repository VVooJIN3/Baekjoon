TC = int(input())

for test_case in range(1, TC + 1):
    N, M = map(int, input().split())
    s = list(input().split())
    t = list(input().split())

    Q = int(input())
    result = []
    for _ in range(Q):
        Y = int(input()) - 1
        result.append(s[int(Y % N)]+ t[int(Y % M)])
    print(f'#{test_case}',end=' ')
    print(*result)
