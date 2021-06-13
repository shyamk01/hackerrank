#Making Anagrams


s1="abc"
s2="amnop"

for x in s1:
        i = s1.find(x)
        j = s2.find(x)
        if j != -1:
            s1 = s1[:i] + s1[i + 1:]
            s2 = s2[:j] + s2[j + 1:]


print(len(s1)+len(s2))