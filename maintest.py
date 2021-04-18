

def diffstr(s):
    arrs = []
    for i in range(len(s)-1):
        if i<=len(s):
            arrs.append(abs(ord(s[i + 1]) - ord(s[i])))
    return arrs
inps="bcxz"
orgstr=diffstr(inps)
revstr=diffstr(inps[::-1])
print(orgstr)
print(revstr)
if orgstr==revstr:
    print("Funny")
else:
    print("Not Funny")
