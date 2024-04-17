import sys
input=sys.stdin.readline

drawing_paper=[[0 for _ in range(100)] for _ in range(100)]
T = int(input())
for _ in range(T):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if drawing_paper[i][j]==1:
                continue
            drawing_paper[i][j]=1
result=0
for row in drawing_paper:
    result+=sum(row)
print(result)