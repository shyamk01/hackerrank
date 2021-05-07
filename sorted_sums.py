s=[4,3,2,1]
sum=0
mod1=(pow(10,9)+7)
for a in range(len(s)+1):
    x=s[0:a]
    x.sort()
    for a in range(0,len(x)):
        sum=sum+(a+1)*x[a]

print(sum%mod1)

