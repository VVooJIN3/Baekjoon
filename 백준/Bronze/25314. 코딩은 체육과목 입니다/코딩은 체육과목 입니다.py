N = int(input())
result=[]

for i in range(1,(N//4)+1):
    result.append('long ')
result.append('int')
result=''.join(result)
print(result)