# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Love Story Mystery
# For the first query, abc → abb → aba.
# For the second query, abcba is already a palindromic string.
# For the third query, abcd → abcc → abcb → abca → abba.
# For the fourth query, cba → bba → aba.
str="adslkfjas"
cnt=0
for a in range(int(len(str)/2)):
    pntbeg=str[a]
    pntend=str[len(str)-1-a]
    if pntbeg!=pntend:
        rs=abs(ord(pntend)-ord(pntbeg))
        cnt=cnt+rs

print(abs(cnt))