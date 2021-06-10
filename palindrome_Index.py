s = "aaab"
if s == s[::-1]:
    print("-1")
else:
    for x in range(len(s)):
        strObj = s[x::]
        #strObj = s[0:x:] + s[x + 1::]
        strObj = strObj[:x] + strObj[x + 1:]
        if strObj == strObj[::-1]:
            print(x)
            break
