a = "11111111111111111111111111111111"
incr = 1
flag = 0
arr = []
for i in range(1, len(a)):
    for j in range(1, len(a) + 2):
        temp1 = incr * j
        if a[0:temp1] != "" and len(a[0:incr * j]) == incr:
            val = a[0:temp1]
            arr.append(val)
        break
    incr = incr + 1

for x in arr:
    str1 = x
    for j in range(1, len(a)):
        str1 += str(int(x) + j)
        if len(str1) >= len(a):
            #str1 = str1[0:len(a)]
            break
    if str1 == a:
        print(str1)
        print("Yes " + x)
        flag = 1
        break
if flag == 0:
    print("No")
