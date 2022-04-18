#k=4

p=[2,7,12,17,22]
k=5

p=list(set(p))
itercomb=[]
final=[]
import itertools
for i in range(1,len(p)+1):
    itercomb=list(itertools.combinations(p,i))
    #print(list(itercomb[0]))
    for ij in range(len(itercomb)):
        #print(itercomb[ij])
        x=list(itertools.combinations(itercomb[ij],2))
        flag=False
        for i in range(len(x)):
            if (x[i][0]+x[i][1])%k==0:
                flag=True

        if flag==False:
            final.append(len(itercomb[ij]))
print(max(final))
# final_itercomb=set()
# for it in range(len(itercomb)):
#     tx=0
#     for i in range(len(itercomb[it])):
#         tx+=itercomb[it][i]
#     print(tx)
#     if tx%k!=0:
#         print("*")
#         print(itercomb[it])
#         print("|")
#         # final_itercomb.add(itercomb[it][0])
#         # final_itercomb.add(itercomb[it][1])
#
# print(final_itercomb)