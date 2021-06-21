s1 = "abcdefghhgfedecba"
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

s1_alp = [0] * 26
for a in s1:
    s1_alp[ord(a) - ord('a')] += 1
x = list(filter(lambda a: a != 0, s1_alp))
flag="NO"
if all_equal(x):
    flag="YES"
else:
    for a in range(len(x)):
        y=list(x)
        y[a]=y[a]-1
        y = [i for i in y if i != 0]
        if all_equal(y):
            flag="YES"
            break
print(flag)



