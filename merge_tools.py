s="AABCAAADA"
k=3

for i in range(0,len(s),k):
    t = ""
    for j in s[i: i + k]:
        if j not in t:
            t += j
    print(t)