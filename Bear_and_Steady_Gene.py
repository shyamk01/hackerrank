s = "ACTGAAAG"
n = len(s) // 4
A=s.count("A")
T=s.count("T")
G=s.count("G")
C=s.count("C")
res = 0
if A != n or C != n or G != n or T != n:
    res = len(s)
    l = 0
    for r in range(len(s)):
        if s[r] == 'A':
            A -= 1
        if s[r] == 'T':
            T -= 1
        if s[r] == 'G':
            G -= 1
        if s[r] == 'C':
            C -= 1
        while A <= n and C <= n and G <= n and T <= n and l <= r:
            res = min(res, r - l + 1)
            if s[l] == 'A':
                A += 1
            if s[l] == 'T':
                T += 1
            if s[l] == 'G':
                G += 1
            if s[l] == 'C':
                C += 1
            l += 1
print(res)