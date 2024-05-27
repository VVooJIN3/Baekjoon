import sys

input=sys.stdin.readline

N=int(input())
stack_temp=[]
stack_line=list(map(int,input().split()))[::-1]
target=1
result="Nice"
while target<=N:
    #print(f'target {target}, line{stack_line}, temp{stack_temp}')
    #줄서있는 곳이 비어있지 않은 경우
    if stack_line:
        #맨 앞 사람이 target과 동일한 경우 pop
        if stack_line[-1] == target:
            stack_line.pop()
            target+=1
            continue
    #line의 맨 앞 서있는 사람이 target이 아닌경우,
    #temp공간에 있는 사람 확인
    if stack_temp and stack_temp[-1] == target:
        stack_temp.pop()
        target+=1
        continue
    #line과 temp 둘 다 target번호와 일치하지 않는경우
    #line에 사람이 남아있으면 temp로 보냄
    if stack_line:
        stack_temp.append(stack_line.pop())
    #line에 사람이 없으면 불가능. 종료
    else:
        result='Sad'
        break


print(result)

