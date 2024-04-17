#(학점*과목평점)의 합/학점 총합
import sys
input=sys.stdin.readline
dic={'A+':4.5,'A0':4.0,
     'B+':3.5,'B0':3.0, 
     'C+':2.5,'C0':2.0,
     'D+':1.5,'D0':1.0,
     'F':0.0}

#학점 총합
total_grade=0.
#과목평점
total_point=0.

for _ in range(20):
    subject, grade, point = input().split()
    grade=float(grade)
    if point=='P':
        continue
    total_grade+=grade
    total_point+=grade*dic[point]

print(total_point/total_grade)
