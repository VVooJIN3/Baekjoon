N=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
result=0
result_arr=[]
for num in arr:
    result=result+num
    result_arr.append(result)
print(sum(result_arr))