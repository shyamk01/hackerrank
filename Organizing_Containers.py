t=[[0, 2,1], [1,1,1],[2,0,0]]
x=len(t)
balldict={}
for i in range(x):
    k = []
    for j in range(x):
        # print("container: "+str(i))
        # print("Ball number: "+str(j))
        # print("How many ball of particular ball number: "+str(t[i][j]))
        k.append(t[i][j])
    balldict[i]=k
print(balldict)

for i,y in balldict.items():
        print(i,y)