# https://www.hackerrank.com/challenges/anagram/problem

s = "xyyx"
cnt = 0
if len(s) % 2 == 0:
    s1 = s[0:(len(s) // 2)]
    s2 = s[(len(s) // 2):]
    for x in s1:
        j= s2.find(x)
        i = s1.find(x)
        if j!=-1:
            s1 = s1[:i] + s1[i+ 1:]
            s2 = s2[:j] + s2[j + 1:]
        else:
            cnt+=1
    print(cnt)
else:
    print("-1")