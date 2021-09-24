t = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]


# 0 ->3
# 1->4
# 2->2

def matrixswap(i, j):
    while (t[i][j] != 0) or (t[j][i] != 0) or (t[i + 1][j] != 0) or (t[j + 1][i] != 0):
        t[i][i] = t[i][i] + 1
        t[i][j] = t[i][j] - 1

        t[j][i] = t[j][i] - 1
        t[j][j] = t[j][j] + 1

        print(i, j, t)
        if (t[i][j] == 0) or (t[j][i] == 0) or (t[i + 1][j] == 0) or (t[j + 1][i] == 0):
            break


for i in range(len(t) - 1):
    for j in range(len(t) - 1):
        if i != j + 1:
            print(i, j + 1)
            matrixswap(i, j + 1)

print(t)
