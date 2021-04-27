from itertools import combinations
def getcorrectsplit(str,n,s):
    setresult=set()
    isprint=False
    perm = combinations(str,n)
    for i in list(perm):
        st=""
        flag=0
        for j in range(0,n):
            a = set(i[j])
            for x in a:
                if i[j].count(x)>1:
                    flag=1
            if flag==0:
                st = st + i[j]
        if st==s:
            setresult.add(i)
            isprint=True
    if isprint==True:
        for i in setresult:
              print(i)
        return isprint

if __name__=='__main__':
    s = 'abacdec'
    str = [s[i: j]
           for i in range(len(s))
           for j in range(i + 1, len(s) + 1)]
    for a in range(len(s)+1):
        if(getcorrectsplit(str,a,s)):
            break