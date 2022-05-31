s="777"
k=0
lenk=len(s)//2
arrfront=""
arrrev=""
arrfinal=[0]*len(s)
flag=False
arrfront=s[0:lenk]
if len(s)%2==0:
    t=s[lenk:len(s)]
    arrrev = t[::-1]
else:
    flag=True
    arrmiddle =s[len(s)%2]
    t = s[lenk+1:len(s)]
    arrrev=t[::-1]
i=0
while(i<len(arrrev)):
        if k==0:
            break
        if k == 1:
            if arrfront[i]==arrrev[i]:
                pass
            else:
                maxval=max(arrrev[i],arrfront[i])
                arrfront = arrfront[:i] + maxval + arrfront[i + 1:]
                arrrev = arrrev[:i] + maxval + arrrev[i + 1:]
                k=k-1

        else:
            if arrfront[i]==arrrev[i]=="9":
                pass
            else:
                maxval = "9"
                arrfront = arrfront[:i] + maxval + arrfront[i + 1:]
                arrrev = arrrev[:i] + maxval + arrrev[i + 1:]
                k=k-2

        i=i+1
final=""
if k==0:
    final=s
if flag==True &k==1:
    final=arrfront+"9"+arrrev[::-1]
else:
    final=arrfront+arrrev[::-1]
if final==final[::-1]:
    print(final)
else:
    print(-1)
