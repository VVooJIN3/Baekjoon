s=input().upper()
values=set(s)

counts=[]
for i in values:
    counts.append(s.count(i))

if counts.count(max(counts))==1:
    values=list(values)
    print(values[counts.index(max(counts))])
else:
    print('?')