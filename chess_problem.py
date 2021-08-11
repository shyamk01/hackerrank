#!/bin/python3

#[[0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 1, 0]]
#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def set_c_q(r_q_temp, c_q_temp):
    r_q = r_q_temp
    c_q = c_q_temp
    return r_q,c_q


def queensAttack(n, k, r_q, c_q, obstacles):
    r_q_temp = r_q
    c_q_temp = c_q
    set_c_q(r_q_temp, c_q_temp)
    if obstacles is not None:
        for i in range(len(obstacles)):
            for j in range(len(obstacles[0])):
                obstacles[i][j] = obstacles[i][j] - 1

    #print(obstacles)
    arr = [[0] * n for i in range(n)]

    # 1
    while (r_q - 1 > 0) and (c_q - 1 > 0):
        r_q = r_q - 1
        c_q = c_q - 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break
    # 2

    r_q, c_q = set_c_q(r_q_temp, c_q_temp)
    while (r_q < n) and (c_q < n):
        r_q = r_q + 1
        c_q = c_q + 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break

    # 3

    r_q, c_q = set_c_q(r_q_temp, c_q_temp)
    while c_q > 1:
        c_q = c_q - 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break

    # 4
    r_q, c_q = set_c_q(r_q_temp, c_q_temp)
    i = 0
    while c_q < n:
        c_q = c_q + 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break

    # 5
    r_q, c_q = set_c_q(r_q_temp, c_q_temp)
    while r_q > 1:
        r_q = r_q - 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break
    r_q, c_q = set_c_q(r_q_temp, c_q_temp)

    # 6

    while r_q < n:
        r_q = r_q + 1
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break
    r_q, c_q = set_c_q(r_q_temp, c_q_temp)

    # 7

    while r_q <= n and c_q <= n and r_q>0 and c_q>0:
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break
        r_q = r_q + 1
        c_q = c_q - 1
    r_q, c_q = set_c_q(r_q_temp, c_q_temp)
    print(arr)
    # 8

    while r_q <= n and c_q <= n and r_q>0 and c_q>0:
        if [r_q - 1, c_q - 1] not in obstacles:
            arr[r_q - 1][c_q - 1] = 1
        else:
            break
        r_q = r_q - 1
        c_q = c_q + 1

    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                cnt += 1
    cnt = cnt - 1
    print(cnt)  # -1 because of queen positions

    # Write your code here
obstacles = []
queensAttack(8 ,0,1,1,obstacles)
