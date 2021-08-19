s="1 1 1 0 1 1 0 0 0 0"
t=list(map(int,s.split(" ")))
k=3
n=10
energy=100-(t[0]*2+1)
i=0
while (i+k)%n!=0:
    t1=(i+k)%n
    energy = energy - (t[t1]*2+1)
    i=i+k
print(energy)

