N=int(input())
prime_number_count=0
arr=list(map(int,input().split()))
for num in arr:
    temp=[]
    for i in range(1,num+1):
        if num%i==0:
            temp.append(i)
    if len(temp)==2:
        prime_number_count+=1
          
print(prime_number_count)
    