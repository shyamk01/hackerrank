p=20
d=3
m=6
s=70
arr=[]


k=0
while(s>=sum(arr)):
    k = k + 1
    if p>=m:
        arr.append(p)
        p=p-d
    else:
        arr.append(m)

print(k-1)
