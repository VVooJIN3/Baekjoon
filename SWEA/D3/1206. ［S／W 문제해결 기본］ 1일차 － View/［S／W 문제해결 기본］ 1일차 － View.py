for test_case in range(1, 11):
    N=int(input())
    arr=list(map(int,input().split()))
    view_count=0
    for i in range(2,N-2):
        diff_arr=[arr[i]-arr[i-2],arr[i]-arr[i-1],arr[i]-arr[i+1],arr[i]-arr[i+2]]
        if min(diff_arr)>0:
            view_count+=min(diff_arr)
    print(f'#{test_case} {view_count}')