#1:1
#2:6 (2~7)
#3:12(8~19)
#4:18(20~37)
#층마다 숫자의 수가 이전의 +6개만큼 증가하는 규칙
N=int(input())
stairs=1
if N>1:
    i=1
    while True:
        i+=6*stairs
        stairs+=1
        if N<=i:
            break
print(stairs)