import os

s = "hackerhappy"
t = "hackerrank"
k = 10

prefix = os.path.commonprefix([s, t])
p = len(prefix)
d = len(s) - p
a = len(t) - p
m = a + d
e = k - m
if e < 0:
    print("No")
if e < 2 * p and e % 2 != 0:
    print("No")
print("Yes")
