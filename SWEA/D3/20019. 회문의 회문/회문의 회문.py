T = int(input())

for test_case in range(1, T + 1):
    s = input()
    N = len(s)
    result = 'NO'
    if s == s[::-1] and s[0:int((N - 1) / 2)] == s[0:int((N - 1) / 2)][::-1] and s[N-int((N - 1) / 2):N] == s[N-int((N - 1) / 2):N][::-1]:
        result = 'YES'
    print(f'#{test_case} {result}')