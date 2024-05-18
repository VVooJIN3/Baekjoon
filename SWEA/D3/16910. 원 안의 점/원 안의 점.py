T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # N이 1일때, x^2+y^2<=1
    s = set()
    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            if i ** 2 + j ** 2 <= N ** 2:
                s.add((i, j))

    print(f'#{test_case} {len(s)}')