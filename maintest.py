numbers1 = [17, 28, 30]
numbers2 = [99, 16, 8]
alice=0
bob=0

for a,b in zip(numbers1,numbers2):
    if a>b:
        alice+=1
    elif a<b:
        bob+=1
    else:
        pass
print(alice,bob)