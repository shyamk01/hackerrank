arr=[11,6,8,7]

possibilities=[]
minimum=min(arr)
for i in range(4):
    final=0
    for k in range(len(arr)):
        diff = arr[k]-minimum
        difffive=diff//5
        difftwo=(diff%5)//2
        diffone=((diff%5)%2)//1
        final+= (difffive+difftwo+diffone)
    minimum=minimum-1
    possibilities.append(final)
print(min(possibilities))





