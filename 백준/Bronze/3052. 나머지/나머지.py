import sys

result=[]
for i in range(10):
  
  result.append(int(sys.stdin.readline())%42)

result=set(result)
print(len(result))