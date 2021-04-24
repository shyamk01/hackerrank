def mincointrev(arrs):
    arrzero=[]
    arrstartone=[]
    for i in range(len(arrs)):
        if i%2==0:
            arrzero.append(0)
            arrstartone.append(1)
        else:
            arrzero.append(1)
            arrstartone.append(0)

    numstartzero = [1 for (x1, x2) in zip(arrzero, arrs) if abs(x1 - x2)==1].count(1)
    numstartone = [1 for (x1, x2) in zip(arrstartone, arrs) if abs(x1 - x2)==1].count(1)
    if numstartzero==0 or numstartone==0:
        print(0)
    elif numstartzero < numstartone:
        print(numstartzero)
    elif numstartone < numstartzero:
        print(numstartone)
    else:
        print(numstartzero)

if __name__=="__main__":
    arrs = [0, 1, 1, 0]
    mincointrev(arrs)