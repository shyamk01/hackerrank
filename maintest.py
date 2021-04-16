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
ars=[]
for _, j in groupby(s):
    sumi=0
    for i in list(j):
        sumi =sumi+ int(alphdict[i])
        ars.append(sumi)
for a in queries:
    if a in ars:
        print("Yes")
    else:
        print("No")

end =round(time.time() * 1000)

print("the time taken to execute the program{f}", end-start)