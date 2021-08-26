a=3
b=9
import math
c=math.sqrt(a)
d= math.sqrt(b)
e=math.ceil(d)-math.ceil(c)
if int(d + 0.5) ** 2 == b:
    print(e+1)
else:
    print(e)



