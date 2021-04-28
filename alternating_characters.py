'''
Alternating Characters
https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
'''
Solutions1 but Terminated due to timeout :(
def alternatingCharacters(s):
    k=0
    j = 0
    while(k<len(s)):
        if (k + 1 <= len(s) - 1) and (s[k] == s[k + 1]):
            s = s[:k] + s[k+1:]
            k=0
            j=j+1
        else:
            k=k+1
    print(j)
'''

def alternatingCharacters(s):
    k=0
    for a in range(len(s)-1):
        if (s[a] == s[a + 1]):
            k=k+1
    print(k)
alternatingCharacters("AAAA")