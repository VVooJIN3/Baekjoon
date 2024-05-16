N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for _ in range(N):
    for i in range(N-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

for i in range(N):
    print(arr[i])