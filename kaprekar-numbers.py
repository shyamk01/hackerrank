def kaprekar_number(n):
    sq = str(n * n)
    t1 = sq[:len(sq) // 2]
    t2 = sq[len(sq) // 2:]
    if t1 == "":
        t1 = 0
    if int(n) == int(t1) + int(t2):
        return n


def kaprekarNumbers(p, q):
    t1 = []
    # Write your code here
    while (p <= q):
        x = kaprekar_number(p)
        if x != None:
            t1.append(str(x))
        p = p + 1

    tp=(' '.join(t1))
    if tp=="":
        print("INVALID RANGE")
    else:
        print(tp)
kaprekarNumbers(400, 700)