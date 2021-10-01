arr=[5, 4, 4, 2, 2, 8]
arr="66 42 68 72 68 81 91 19 40 73 44 73 89 73 44 12 77 40 44 17 59 99 35 92 80 51 14 30"
arr=list(map(int,arr.split(" ")))
ls=[]
def cutTheSticks(arr):
    # Write your code here
    for i in range(len(arr)):
        if len(arr)>0:
            arr=[arr[k] for k in range(len(arr)) if arr[k]!=0]
            if len(arr)>0:
                ls.append(len(arr))
                x=min(arr)
                arr = [arr[k]-x for k in range(len(arr)) if arr[k] != 0]

    return ls
print(cutTheSticks(arr))


