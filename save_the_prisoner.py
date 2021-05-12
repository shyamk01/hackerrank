def saveThePrisoner(n, m, s):
    r =m%n
    if r+s-1%n==0:
        return n
    else:
        return r+s-1%n

n=7
m=19
s=2
print(saveThePrisoner(n, m, s))

