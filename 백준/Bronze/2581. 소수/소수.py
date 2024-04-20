M=int(input())
N=int(input())

prime_number_sum=0
prime_number_arr=[]
for num in range(M,N+1):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:
        prime_number_arr.append(num)
if len(prime_number_arr)>0:
    for prime_number in prime_number_arr:
        prime_number_sum+=prime_number
    print(prime_number_sum)
    print(prime_number_arr[0])
else :
    print("-1")