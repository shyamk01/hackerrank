def saveThePrisoner(n, m, s):
    r =m%n
    if r+s-1%n==0:
        return n # this will be when you distribute all the candy into the prisoner, then last prisoner will get the candy
    else:
        return r+s-1%n

n=7
m=19
s=2
print(saveThePrisoner(n, m, s))

