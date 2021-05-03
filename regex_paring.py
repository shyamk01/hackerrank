# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Re.findall() & Re.finditer()
# without regular expression but hackerrank expected solutions in regular expression
s="match a single character not present in the list below"
x=['a','e','i','o','u','A','E','I','O','U']
k=0
str = ""
while(k<len(s)):
    prev = 0
    last = 0
    if s[k] in x and k+1<len(s):
        if s[k+1] in x:
            prev = k
            str=str+s[k]
        else:
            str = str + s[k]+"*"

    k=k+1
if s[k-1] in x:
    str=str[0:str.rindex("*")]

a=[print(x) for x in str.split("*") if len(x)>1 ]

# # Below code take into the pictures due to last characters is vowels
# t=len(a)
# if s[k-1] in x:
#     t=len(a)-1
# for x in range(t):
#     print(a[x], end="\n")
if len(a)==0:
    print(-1)