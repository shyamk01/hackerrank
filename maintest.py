from string import ascii_lowercase
from collections import Counter
from itertools import groupby

s = "abccddde"
queries=[5,9,7,8,12,5]
import  time
start= round(time.time() * 1000)
alphabet = sorted(set(ascii_lowercase))
enlist = enumerate(alphabet, 1)
alphdict=dict((j,i) for i,j in enlist)
print(alphdict)
ars=set()
ctr=1
for i in range(len(s)):
    value = alphdict[s[i]]
    if(i+1!=len(s) and s[i+1]==s[i]):
        ctr=ctr+1
    else:
        ctr=1
    ars.add(ctr*value)
for a in range(len(queries)):
    "Yes" if queries[a] in ars else "No"
end =round(time.time() * 1000)

print("the time taken to execute the program{f}", end-start)