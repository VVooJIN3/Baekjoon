N=int(input())
arr=[]
for _ in range(N):
    x, y = map(int,input().split())
    arr.append([x,y])

arr=sorted(arr,key=lambda x : (x[1],x[0]))
max_time=arr[0][1]
result=1
for i in range(1,N):
    if max_time<=arr[i][0]:
        max_time=arr[i][1]
        result+=1

print(result)