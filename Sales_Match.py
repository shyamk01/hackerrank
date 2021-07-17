ar=[1,2,1,1,3,2]
t=set(ar)
x=0
for a in t:
    tx=ar.count(a)
    x+=tx//2

print(x)
