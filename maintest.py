arr = [-4, 3, -9, 0, 4, 1]
plus = 0
minus = 0
zero = 0
lenarr = len(arr)
for i in arr:
    if i > 0:
        plus += 1
    if i < 0:
        minus += 1
    if i == 0:
        zero += 1

print(str.format('{0:.6f}', plus / lenarr))
print(str.format('{0:.6f}', minus / lenarr))
print(str.format('{0:.6f}', zero / lenarr))

