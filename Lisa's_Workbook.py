n = 1
k = 1
arr = [100]
inrcnt = 0
cnt=0
arr_final = []

for j in range(len(arr)):
    for kj in range(arr[j]):
        arr_final.append(kj + 1)
print(arr_final)

for ki in range(len(arr_final)):
    if arr_final[ki] == 1 or arr_final[ki]%k==1:
        inrcnt = inrcnt + 1
        if arr_final[ki]==inrcnt:
            cnt+=1
    elif arr_final[ki]==inrcnt:
            cnt+=1
    elif k==1:
        cnt+=1
print(cnt)