debts = [['Alex', 'Blake', '5'], ['Blake', 'Alex', '3'], ['Casey', 'Alex', '7'], ['Casey', 'Alex', '4'],
         ['Casey', 'Alex', '2']]
debts = [['Blake', 'Alex', '7'], ['Blake', 'Alex', '3'], ['Alex', 'Blake', '4'], ['Blake', 'Alex', '1'],
         ['Alex', 'Blake', '7']]
borrower = {}
lender = {}
for a in debts:
    if a[0] in borrower.keys():
        borrower[a[0]] = int(borrower.get(a[0])) + int(a[2])
    else:
        borrower[a[0]] = a[2]
    if a[1] in lender.keys():
        lender[a[1]] = int(lender.get(a[1])) + int(a[2])
    else:
        lender[a[1]] = a[2]

print(borrower)
print(lender)
smallneg={}
allkey = set().union(borrower,lender)
for ax in allkey:
    if ax in borrower.keys() and ax in lender.keys():
        ayz=int(lender[ax])-int(borrower[ax])
        smallneg[ax]=ayz
    elif ax in borrower.keys():
        smallneg[ax] = - int(borrower[ax])
    elif ax in lender.keys():
        smallneg[ax] = - int(lender[ax])

print(smallneg)
temp = min(smallneg.values())
if temp>0:
    res = [key for key in smallneg if smallneg[key] == temp]
    print(res)
else:
    print("Nobody has a negative balance")