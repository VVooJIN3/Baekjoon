T= int(input())

for _ in range(T):
    C=int(input())
    Q,tmp=divmod(C,25)
    D,tmp=divmod(tmp,10)
    N,P=divmod(tmp,5)
    print(f'{Q} {D} {N} {P}')
