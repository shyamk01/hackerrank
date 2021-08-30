x=8
y=8

r=[(0,0),(0,1),(1,0),(1,1)]

x=x%4
y=y%4
print(x,y)
if (x-1,y-1) in r:
    print("Second")
else:
    print("First")

