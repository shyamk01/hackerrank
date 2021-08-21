s="if man was meant to stay on the ground god would have given us roots"
s=s.replace(" ","")
import math
t=math.sqrt(len(s))
st=math.floor(t)
et=math.ceil(t)
arr=[]
for i in range(0,len(s),et):
    t=s[i:i+et]
    t1=t+((et-len(t))*"$")
    arr.append(t1)
columns = list(zip(*arr))

for x in columns:
    print("".join(list(x)).replace("$",""))

