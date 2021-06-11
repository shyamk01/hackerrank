
def palindrome(s):
    if s == s[::-1]:
        return -1
    else:
        for x in range(len(s)//2):
            if s[x] != s[len(s) - x - 1]:
                t = s[:x] + s[x + 1:]
                if t == t[::-1]:
                    return x
                else:
                    return len(s)-x-1

print(palindrome("aaab"))