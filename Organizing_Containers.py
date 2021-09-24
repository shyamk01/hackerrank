t = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]

t1 = []
t2 = []

for i in range(len(t)):
    s = 0
    s1=0
    for j in range(len(t)):
        s = s + (t[i][j])
        s1 = s1 + (t[j][i])
    t1.append(s)
    t2.append(s1)

if sorted(t1)==sorted(t2):
    print("Possible")
else:
    print("Impossible")
