n=5
queries=[[1, 2, 100], [2, 5, 100], [3, 4, 100]]
a=[0]*n
t=[0]*n

for qa in queries:
    t1=qa[0]-1
    t2=qa[1]
    sm=qa[-1]
    a[t1:t2] = [sm] * (t2 - t1)
    for tx in range(t1,t2,1):
        t[tx]+=a[tx]


print(max(t))