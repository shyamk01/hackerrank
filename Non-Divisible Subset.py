from itertools import combinations
k1=7
def checknotdivisible(rt):
    ks=list(combinations(rt,2))
    flag=False
    for x in ks:
        if sum(x)%k1==0:
            flag=True

    if flag==False:
        return rt


s="278 576 496 727 410 124 338 149 209 702 282 718 771 575 436"
s=list(map(int,s.split(" ")))
t=set(s)

tz=[]
for a in range(len(s)):
    k=list(combinations(t,a+2))
    tz.append(k)
trs=set()
for iz in tz:
    for x in iz:
        rst=checknotdivisible(x)
        if rst!=None:
            trs.add(len(rst))

print(max(trs))



