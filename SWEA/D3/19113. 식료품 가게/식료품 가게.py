TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    printed_price = list(map(int, input().split()))
    discount_price = []
    normal_price = []
    # 할인가격 = 정상가격 *0.75
    i = 0
    while i < N * 2:
        if printed_price[i]==0:
            i+=1
            continue
        if int(printed_price[i] / 0.75) in printed_price:
            discount_index=printed_price.index(int(printed_price[i] / 0.75))
            normal_price.append(int(printed_price[i] / 0.75))
            discount_price.append(printed_price[i])
            printed_price[discount_index]=0
        i += 1

    print(f'#{test_case}', end=' ')
    print(*discount_price)


