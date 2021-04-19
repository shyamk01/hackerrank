n=2
m=6
import  itertools
arrs=[]

def gcd(a,b):
    if b==0:
        return a
    return gcd(a,a%b)

for i in range(1, m+1):
    if m%i==0:
        arrs.append(i)
print(arrs)
lst = list(itertools.permutations(arrs,n))

arrgcd=[]
for i in lst:
    if gcd(i[0],i[1])==1:
        arrgcd.append(i)

print(len(arrgcd))
