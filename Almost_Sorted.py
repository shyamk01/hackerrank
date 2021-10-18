# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
s = "43 65 1 98 99 101"
#s = "4 2"
s="1 5 4 3 2 6"
s="43 65 1 98 99 101"
s = list(map(int, s.split(" ")))
k = []


def isSwap(arr):
    flag = False
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            k.append(j + 1)
            if len(k) > 2:
                flag = True
                k.clear()
                break
    if flag:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                k.append(j + 1)


def almostSorted(arr):
    n=len(arr)
    sortedarr = sorted(arr)
    a = []
    subarr = []
    ctr = 0
    for i in range(n):
        if arr[i] != sortedarr[i]:
            ctr += 1
            a.append(i + 1)
    print(a)
    print(ctr)
    if ctr == 2:
        print("yes")
        print("swap", a[0], a[1], sep=" ")
    else:
        for i in range(n):
            if arr[i] == sortedarr[i]:
                None
            else:
                subarr.append(arr[i])
        if subarr == sorted(subarr, reverse=True):
            print("yes")
            print("reverse", arr.index(subarr[0]) + 1, arr.index(subarr[-1]) + 1, sep=" ")
        else:
            print("no")


almostSorted(s)
