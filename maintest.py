s = "hacakaeararanaka"
match = "hackerrank"
i = 0

for x in s:
    if i<= len(match)-1:
        if (match[i] == x):
            i = i + 1

if i != len(match):
    print("No")
else:
    print("Yes")
