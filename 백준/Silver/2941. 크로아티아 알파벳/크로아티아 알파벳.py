alphabet=['c=','c-','dz=','d-','lj','nj','s=','z=']

s=input()

for i in alphabet:
    if i in s:
        s = s.replace(i,'1')
print(len(s))    