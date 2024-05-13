from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    s = set()
    s.add(0)
    
    for num in arr:
        new_s = set()
        for s_num in s:
            new_s.add(num+s_num)
        s |= new_s
        
    print(f'#{test_case} {len(s)}')


