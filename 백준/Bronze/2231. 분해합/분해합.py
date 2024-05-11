N=int(input())
minimum_constructor = 0
for num in range(N-1,-1,-1):
    num_arr=[]
    for i in range(len(str(num))):
        num_arr.append(int(str(num)[i]))
    if num+sum(num_arr)==N:
        minimum_constructor=num
print(minimum_constructor)    
