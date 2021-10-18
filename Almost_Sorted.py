# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
s = "43 65 1 98 99 101"
# s = "4 2"
s = "1 5 4 3 2 6"
s = list(map(int, s.split(" ")))
k = []

def almostSorted(s):
    sortedarr = sorted(s)
    a = []
    subarr = []
    ctr = 0
    for i in range(len(s)):
        if s[i] != s[i]:
            ctr += 1
            a.append(i + 1)
    if ctr == 2:
        print("yes")
        print("swap", a[0], a[1], sep=" ")
    else:
        for i in range(len(s)):
            if s[i] == sortedarr[i]:
                None
            else:
                subarr.append(s[i])
        if subarr == sorted(subarr, reverse=True):
            print("yes")
            print("reverse", s.index(subarr[0])+1,s.index(subarr[-1])+1,sep=" ")
        else:
            print("no")


almostSorted(s)
