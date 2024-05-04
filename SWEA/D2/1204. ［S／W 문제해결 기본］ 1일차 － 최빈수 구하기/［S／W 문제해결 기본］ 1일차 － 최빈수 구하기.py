T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    arr=list(map(int,input().split()))
    max_count=0
    result=0
    count=0
    for num in arr:
        while num in arr:
            count+=1
            arr.remove(num)
        if count>max_count:
            max_count=count
            result=num
        elif count==max_count and result < num:
            result=num
        count=0    
    print(f'#{test_case} {result}')