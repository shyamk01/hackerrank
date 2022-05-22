def kangaroo(x1, v1, x2, v2):
    a1 = [0] * 10000
    b1 = [0] * 10000
    a1[0] = x1
    b1[0] = x2
    tx1=0
    tx2=0
    for i in range(1, len(a1)):
        tx1 = a1[i-1]+v1
        tx2 = b1[i-1]+v2
        a1[i] = tx1
        b1[i] = tx2

        if a1[i] == b1[i]:
            return "YES"
            break
        if i == len(a1)-1:
            return "NO"
    # Write your code here
