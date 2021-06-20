s = "cdefghmnopqrstuvw"
letterCnt = [0] * 26
oddcnt = 0
found = True
for letter in s:
    letterCnt[ord(letter) - ord('a')] += 1

for a in letterCnt:
    oddcnt += a % 2

print(oddcnt)

if oddcnt > 1:
    found = False

if not found:
    print("No")
else:
    print("Yes")