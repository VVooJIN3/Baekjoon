arr_x=[]
arr_y=[]
for _ in range(3):
    x, y =map(int,input().split())
    arr_x.append(x)
    arr_y.append(y)
for i in range(3):
    diff_x=arr_x.pop(i)
    if diff_x not in arr_x:
        solution_x=diff_x
        break
    else:
        arr_x.insert(i,diff_x)

for j in range(3):
    diff_y=arr_y.pop(j)
    if diff_y not in arr_y:
        solution_y=diff_y
        break
    else:
        arr_y.insert(j,diff_y)
print(solution_x,solution_y)