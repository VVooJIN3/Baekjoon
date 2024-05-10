T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #재료의 수 N, 제한 칼로리 L
    N, L = map(int,input().split())
    scores=[]
    cals=[]
    maximum=0
    for i in range(N):
        s, c = map(int,input().split())
        scores.append(s)
        cals.append(c)
    max_score = 0
    
    def dfs(count, score, cal):
        global max_score
        #칼로리를 초과하는 경우 돌아가기
        if cal > L:            
            return
        # 현재 점수가 최고점수를 초과한 경우 갱신 
        if score > max_score : 
            max_score = score
        # 모든 재료를 사용한 경우, 이전으로 돌아가기
        if count==N: 
            return
        #해당 재료를 선택했을 때
        dfs(count+1, score + scores[count], cal + cals[count])
        #해당 재료를 선택하지 않았을 때->count만 증가
        dfs(count+1, score, cal) 
    dfs(0,0,0)
    print(f'#{test_case} {max_score}')
    
    