arr=[]
for _ in range(3):
    arr.append(int(input()))
arr_set=set(arr)
if len(arr_set)==1 and 60 in arr_set:
    result='Equilateral'
elif sum(arr)==180 and len(arr_set)==2:
    result='Isosceles'
elif sum(arr)==180 and len(arr_set)==3:
    result='Scalene'
elif sum(arr)!=180:
    result='Error'
print(result)