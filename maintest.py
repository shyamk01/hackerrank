arr=[396285104,573261094,759641832,819230764,364801279]
#arr=[140638725,436257910,953274816,734065819,362748590]
#arr=[1,2,3,4,5]

min=0
max=0
flag =1
for i in range(len(arr)):
    arsum = sum(arr[:i] + arr[i + 1:])
    if ((arsum < max) & flag):
        min=arsum
        flag=0
    if ((flag==0) & (arsum <min)):
        min = arsum

    if max < arsum:
        max = arsum


print(min)
print(max)