values=[]
for i in range(9):
    values.append(int(input()))
print(max(values))
print(values.index(max(values))+1)