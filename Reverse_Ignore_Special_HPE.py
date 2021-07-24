inp = "Ab,c,de!$"
inplst = list(inp)
# Output:  str = "c,b$a"
# ed,c,bA!$
sp_ch = [',', '$', '!']
str1 = list(inp)
str2 = ''.join(filter(str.isalnum, inp))
t = str2[::-1]
i = 0
for a in range(0, len(inp)):
    while i <= len(t)-1:
        if inp[a] not in sp_ch:
            str1[a] = t[i]
            i = i + 1
        break
print(''.join(str1))
