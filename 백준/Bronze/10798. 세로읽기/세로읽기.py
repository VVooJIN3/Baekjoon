str=[]
max_len=0
for i in range(5):
    temp=list(input())
    str.append(temp)
    if max_len < len(temp) :
        max_len = len(temp) 

for i in range(max_len):
    for s in str:
      try:
        print(s[i],end='')
      except:
        continue