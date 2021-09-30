s="abcd"
t="abcdert"
k=10
s=list(s)
t=list(t)
l=min(len(s),len(t))


for i in range(l):
    if s[i]!=t[i]:
        s[i]=-1
        t[i]=-1
    else:
        break
s = [x for x in s if x != -1]
t = [x for x in t if x != -1]

if len(s)+len(t)<=k :
    print("Yes")
else:
    print("No")