x = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"
x="66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"
x=list(map(int, x.split(" ")))
res = list(set(x))
arr = []
for a in range(len(res) - 1):
    res1 = set()
    if abs(res[a + 1] - res[a] == 0) or abs(res[a + 1] - res[a] == 1):
        res1.add(res[a])
        res1.add(res[a + 1])
        arr.append(res1)

for x2 in range(len(res)):
    arr.append({res[x2]})

arr2 = []
for ax in arr:
    x1 = []
    for j in ax:
        for m in x:
            if m == j:
                x1.append(j)
    arr2.append(len(x1))

print(max(arr2))
