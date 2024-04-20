import sys
input=sys.stdin.readline

while True:
    n=int(input())
    if n==-1:
        break
    else:
        cnt=1
        divisor_sum=0
        arr=[]
        message=f"{n}"
        for i in range(1,n):
            if n%i==0:
                divisor_sum+=i
                arr.append(i)
        if divisor_sum==n:
            message+=f" = "
            for divisor in arr:
                message+=f"{divisor} + "
            print(message[0:-2])
        elif divisor_sum!=n:
            message+=" is NOT perfect."
            print(message)