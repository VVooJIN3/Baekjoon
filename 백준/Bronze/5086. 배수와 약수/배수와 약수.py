import sys
input = sys.stdin.readline
while True:
    N, M = map(int,input().split())
    if M==0 and N==0:
        break
    elif M%N==0:
        result='factor'
    elif N%M==0:
        result='multiple'
    else:
        result='neither'
    print(result)