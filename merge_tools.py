s="AABCAAADA"
k=3
def make_link(arr):
    G = []
    s=""
    for i in arr:
        if i not in G:
            G.append(i)
            s+=i
    return s



make_link('abcdefgha');
for i in range(0,len(s),k):
    print(make_link(s[i:i+k]))