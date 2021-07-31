q = "1 2 5 3 4 7 8 6"
q= list(map(int,q.split(" ")))

c = 0
flag = 0
for i in range(len(q) - 1, 0, -1):
    if q[i] != i + 1:
        if q[i - 1] == i + 1:
            c += 1
            q[i], q[i - 1] = q[i - 1], q[i]
        elif q[i - 2] == i + 1:
            c += 2
            q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
            q[i - 1], q[i] = q[i], q[i - 1]
        else:
            flag = 1
            break

if flag == 1:
    print("Too chaotic")
else:
    print(c)