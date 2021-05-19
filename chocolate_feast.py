n = 20373
c = 18211
m = 10188

choc = n // c
wrap = n // c
if wrap >= m:
    while wrap != m:
        x = wrap // m
        choc = choc + x
        wrap = x + (wrap % m)
    print(choc + 1)
else:
    print(choc)
