
for test_case in range(1, 11):
    dump=int(input())
    arr=list(map(int,input().split()))
    for _ in range(dump):
        min_value=min(arr)
        max_value=max(arr)
        if max_value - min_value <=1:
            break
        min_index=arr.index(min_value)
        max_index=arr.index(max_value)
        arr[max_index]-=1
        arr[min_index]+=1
    print(f'#{test_case} {max(arr)-min(arr)}')
    