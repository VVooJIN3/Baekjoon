N=int(input())
group_count=0
for _ in range(N):
    str=input()
    arr=[]
    boolean=True
    arr.append(str[0])
    for i in range(0,len(str)-1):
        if str[i]==str[i+1]:
            continue
        else:
            if str[i+1] not in arr:
                arr.append(str[i+1])
            else :
                boolean=False
                break
    if boolean:
        group_count+=1
               
print(group_count) 