while True:
    arr = list(map(int,input().split()))
    arr_set=set(arr)
    if len(arr_set)==1 and 0 in arr_set:
        break
    elif sum(arr)-max(arr)<=max(arr):
        result='Invalid'
    elif len(arr_set)==1:
        result='Equilateral'
    elif len(arr_set)==2:
        result='Isosceles'
    elif len(arr_set)==3:
        result='Scalene'
    print(result)