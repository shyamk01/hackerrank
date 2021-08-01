n=5
queries=[[1, 2, 100], [2, 5, 100], [3, 4, 100]]
a=[0]*(n+1)
t=[0]*(n+1)

for qa in queries:
    t1 = qa[0]-1
    t2 = qa[1]
    sm = qa[-1]
    a[t1]+=sm
    a[t2]+=-sm

max=sum=0
for i in a:
    sum+=i
    if sum>max:
        max=sum


print(max)