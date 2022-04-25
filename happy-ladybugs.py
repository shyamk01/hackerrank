s = "RBY_YBR"


def happy(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1 and s[i] != '_':
            return "NO"

    if s.count("_") == 0:
        for i in range(1, len(s) - 1):
            if s[i] != s[i - 1] and s[i] != s[i + 1]:
                return "NO"

        if s[-1] != s[-2]:
            return "NO"

    return "YES"


print(happy(s))
