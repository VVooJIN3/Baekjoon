#중앙이동 알고리즘
#1. 정사각형 각 변 중앙에 점을 하나 추가한다
#2. 정사각형 중심에 점을 하나 추가한다.
#과정0=점4,   사각형1
#과정1=점9,   사각형4 
#과정2=점25,  사각형16
#...
#규칙 : 사각형은 2^(N-1)x2^(N-1)만큼 생성됨 (N : 시행횟수)
#추가되는 점의 갯수 규칙
#ex)N이 3일때= 사각형은 4x4일때 생성되는 점의 갯수
#5 4 4 4
#4 3 3 3
#4 3 3 3
#4 3 3 3

#함수로 구현
# def add_dot(length):
#     dot=0
#     for i in range(length):
#         for j in range(length):
#             if i==0:
#                 if j==0:
#                     dot+=5
#                 else :
#                     dot+=4
#             else :
#                 if j==0:
#                     dot+=4
#                 else :
#                     dot+=3
#     return dot
# N=int(input())
# #정사각형을 이루는 점 4개(초기값)
# dot=4
# for i in range(1,N+1):
#   length=2**(i-1)
#   dot+=add_dot(length)
#   print(dot)
# print(dot)

#시간초과 => 해당 방법 폐기. 
#결과 규칙:
#N=1 :9    (3^2) 
#N=2 :25   (5^2) +2
#N=3 :81   (9^2) +4
#N=4 :289  (17^2)+8
#N=5 :1089 (33^2)+16

N=int(input())
#정사각형을 이루는 점 4개(초기값)
num=2
for i in range(N):
    num+=2**(i)
print(num**2)