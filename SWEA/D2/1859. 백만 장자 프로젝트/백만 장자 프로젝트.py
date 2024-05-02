T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result=0
    N=int(input())
    arr=list(map(int,input().split()))
    #물건이 가장 비싼 날짜
    max_index=arr.index(max(arr))
    while len(arr) !=1:
        if max_index == 0 and len(arr)>=2:
          arr=arr[max_index+1:]
          max_index=arr.index(max(arr))
          continue
        for i in range(0,max_index):
        	result+=arr[max_index]-arr[i]
        if max_index == len(arr)-1:
                break
        arr=arr[max_index+1:]
        max_index=arr.index(max(arr))
    print(f'#{test_case} {result}')