t=['BBBGBGBBB', 'BBBGBGBBB', 'BBBGBGBBB', 'GGGGGGGGG', 'BBBGBGBBB', 'BBBGBGBBB', 'GGGGGGGGG', 'BBBGBGBBB', 'BBBGBGBBB', 'BBBGBGBBB']


r = 10
c = 9

def replaceS(s,x,y):
    new_character = 'B'
    st = s[x]
    st1 = st[:y] + new_character + st[y + 1:]
    s[x]=st1
    return s

kl = min(r, c)
final = []
final2 = []
final.append(1)

for i in range(r):
    for j in range(c):
        if t[i][j] == 'G':
            for k in range(kl):
                if 0 <= i - k < r and 0 <= i + k < r and 0 <= j - k < c and 0 <= j + k < c:
                    if t[i - k][j] == 'G' and t[i + k][j] == 'G' and t[i][j - k] == 'G' and t[i][j + k] == 'G':
                        tx = 1 + 4 * k
                        if tx != 1:
                            print(i, j, k, 1 + 4 * k)
                            t1 = i, j, k, 1 + 4 * k
                            final2.append(t1)
                    else:
                        break

print(final2)
final_test=[]
for x in final2:
    t=x[2]
    kt=0
    arr_test = []
    while kt<t:
        kt=kt+1
        tx1=x[0], x[1] - kt
        tx2=x[0], x[1] + kt
        tx3=x[0]-kt, x[1]
        tx4=x[0]+kt, x[1]
        arr_test.append(tx1)
        arr_test.append(tx2)
        arr_test.append(tx3)
        arr_test.append(tx4)
    cd = x[0], x[1]
    arr_test.append(cd)
    final_test.append(arr_test)
print(final_test)
set_final = []
if len(final_test)!=0:
    for i in final_test:
        for j in final_test:
            if j != i:
                res = [ele1 for ele1 in i for ele2 in j if ele1 == ele2]
                if len(res) == 0:
                    t = (len(i)) * (len(j))
                    set_final.append(t)

    if len(set_final)==0:
        if len(final_test[0])>0:
            set_final.append(len(final_test[0]))
else:
    set_final.append(1)
print(set_final)
print(max(set_final))
