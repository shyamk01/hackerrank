def biggerIsGreater(d):
    d=list(d)
    i = len(d) - 1
    while i > 0 and d[i - 1] >= d[i]:
        i -= 1
    if i <= 0:
        return ("no answer")
    pivot=i-1
    value=d[pivot]
    reppivot=-1
    for j in reversed(range(len(d))):
        if value < d[j]:
            reppivot = j
            break

    d[pivot], d[reppivot] = d[reppivot], d[pivot]
    t=d[0:pivot+1]+sorted(d[pivot+1:])
    x1="".join(t)
    return x1

    return "".join(arr)

s="dcbb"
print(biggerIsGreater(s))