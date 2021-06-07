s = "asvkugfiugsalddlasguifgukvsa"
def isAlternative(s):
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            return False
    if s[0]==s[1]:
        return False
    return True
a = list(set(s))
import re
a.sort()
print(a)
t=len(a)
sarray=[]
second=""
for x in range(len(a) - 1):
    for j in range(x+1,len(a)):
        z="[^"+a[x]+a[j]+"]*"
        s1= "".join(re.split(z,s))
        if(isAlternative(s1)):
            sarray.append(s1)

if len(sarray)>0:
    start=sarray[0]
    for a in sarray:
        if len(a)>len(start):
            start=a
    print(len(start),start)
else:
    print(0)


