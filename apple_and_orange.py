def countApplesAndOranges():
    s=2
    t=3
    a=1
    b=5
    apples=[2]
    oranges=[-2]
    final_apples=0
    final_oranges=0
    for i in range(len(apples)):
        t1=apples[i]+a
        if t1>=s and t1<=t:
            final_apples+=1
    for i in range(len(oranges)):
        t1= oranges[i] + b
        if t1 >= s and t1 <= t:
            final_oranges+=1
    print(final_apples)
    print(final_oranges)
countApplesAndOranges()