T = int(input())
for test_case in range(1, T + 1):

    n = int(input())
    # 일 월 화 수 목 금 토
    day_arr = list(map(int, input().split()))
    minimum = 700000
    start_index = day_arr.index(1)
    for i in range(start_index,7):
        n_count = n
        day_count = 0
        while n_count != 0:
            for j in range(i, i + 7):
                if n_count == 0:
                    break
                temp = j
                if temp >= 7:
                    temp -= 7
                if day_arr[temp] == 0:
                    day_count += 1
                    continue
                elif day_arr[temp] == 1:
                    day_count += 1
                    n_count -= 1

        if minimum > day_count:
            minimum = day_count

    print(f'#{test_case} {minimum}')


