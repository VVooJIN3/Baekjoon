max_value=0
max_x=0
max_y=0
for i in range(9):
    temp=list(map(int,input().split()))
    if max_value<max(temp):
        max_value=max(temp)
        max_x=i
        max_y=temp.index(max_value)

print(max_value)
print(max_x+1, max_y+1)
    