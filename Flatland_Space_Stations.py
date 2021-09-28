n=6
c=[0,1,2,3,4,5]
def mindist(k):
    tx=[]
    min_d=k
    max_d=k
    while min_d>=0:
        if arr[min_d]==1:
            tx.append(abs(min_d-k))
            break
        min_d=min_d-1
    while max_d<=len(arr):
        if arr[max_d]==1:
            tx.append(abs(max_d-k))
            break
        max_d=max_d+1
    return min(tx)

arr=[0]*n
for i in c:
   arr[i]=1

dis=[]
for i in range(len(arr)):
    if arr[i]==1:
        dis.append(0)
    else:
        dis.append(mindist(i))

print(max(dis))
