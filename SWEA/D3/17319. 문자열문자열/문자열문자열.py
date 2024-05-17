T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = input()
    result = "No"
    if s[0:int(N / 2)] == s[int(N / 2):N]:
        result = "Yes"
    print(f'#{test_case} {result}')
