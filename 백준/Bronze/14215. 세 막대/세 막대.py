arr=list(map(int,input().split()))
max_index=arr.index(max(arr))

if sum(arr)-max(arr)<=max(arr):
    arr[max_index]=sum(arr)-max(arr)-1
print(sum(arr))