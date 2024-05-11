def find_xy(a,b,c,d,e,f):
    for x in range(-999,1000):
        for y in range(-999,1000):
            if c==a*x+b*y and f==d*x+e*y:
                return x,y

a,b,c,d,e,f = map(int,input().split())
x, y = find_xy(a,b,c,d,e,f)
print(x,y)