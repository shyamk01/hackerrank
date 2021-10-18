# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
s = "43 65 1 98 99 101"
#s = "4 2"
s="1 5 4 3 2 6"
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


def almostSorted(s):
    isSwap(s)
    if len(k) <= 2:
        print("yes")
        if len(k) == 1:
            print("swap " + str(k[0]) + " " + str(k[0] + 1))
        else:
            print("swap " + str(k[0]) + " " + str(k[1] + 1))
    else:
        print("yes")
        print("reverse " + str(k[0]) + " " + str(k[-1] + 1))


almostSorted(s)
