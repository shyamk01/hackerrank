t = [0, 0, 1, 0, 0,1,0]
z = len(t)
tz = 0
cnt = 0
while tz < z:
    if ((tz + 2) < z) and (t[tz + 2] == 0):
            cnt = cnt + 1
            tz = tz + 2
    elif ((tz + 1) < z) and (t[tz + 1] == 0):
            cnt = cnt + 1
            tz = tz + 1
    else:
        tz=tz+1

print(cnt)
