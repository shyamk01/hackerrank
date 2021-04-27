'''
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.
e.g.abc->cba
Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.
https://www.hackerrank.com/challenges/funny-string/problem?h_r=next-c%E2%80%A6%E2%80%A6hallenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

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