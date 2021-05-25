a = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
b = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

seto = set(a)
setm = set(b)
for an in setm:
    xa = a.count(an)
    ma = b.count(an)
    if xa != ma:
        print(an)
