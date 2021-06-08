import itertools
test_str = "bccb"

xt=set()
cst = 0
for a in range(len(test_str)):
    if test_str[a] in xt:
           pass
    else:
           xt.add(test_str[a])
           cst+=1
print(cst)

