
def mindist(arr,k):
    tx=[]
    min_d=k
    max_d=k
    while min_d>=0:
        if arr[min_d]==1:
            tx.append(abs(min_d-k))
            break
        min_d=min_d-1
    while max_d<len(arr):
        if arr[max_d]==1:
            tx.append(abs(max_d-k))
            break
        max_d=max_d+1
    return min(tx)
# Complete the flatlandSpaceStations function below.

def flatlandSpaceStations(n, c):
    arr=[0]*n
    for i in c:
        arr[i]=1

    dis=[]
    for i in range(len(arr)):
        if arr[i]==1:
            dis.append(0)
        else:
            dis.append(mindist(arr,i))

    return max(dis)

print(flatlandSpaceStations(20,[13,1,11,10,6]))