N = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result=[]
for number in range(1,N+1):
    str_number=str(number)
    clap=''
    for s in str_number:
        if '3'==s or '6'==s or '9'==s:
            clap+='-'
    if '-' in clap:
        result.append(clap)
    else :
        result.append(number)
print(*result)