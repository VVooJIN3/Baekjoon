
for test_case in range(1, 11):
    N=int(input())
    search=input()
    s=input()
    count=0
    while search in s:
        s = s.replace(search,'',1)
        count+=1
    print(f'#{N} {count}')