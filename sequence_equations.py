p = [2, 3, 1]
p = [4, 3, 5, 1, 2]
#https://www.hackerrank.com/challenges/permutation-equation/problem
arrp = []
for a in range(1, len(p) + 1):
    x = 0
    while x != len(p):
        if a == p[x]:
            y = x + 1
            arrp.append(y)
        x = x + 1

for a in range(0, len(arrp)):
    x = 0
    while x != len(p):
        if arrp[a] == p[x]:
            print(x+1)
        x = x + 1
