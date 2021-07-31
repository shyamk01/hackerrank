a=[1,3,5,2,4,6,7]
cnt=0
for ix in range(len(a)):
    if a[ix]!=ix+1:
        cnt+=1
        t=a.index(ix+1)
        a[ix],a[t]=a[t],a[ix]


print(cnt)
