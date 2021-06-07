a = "ZZYYZZZA"
b = "ZZYYZZZB"
# ZZYYZZYYZZZAZZZB
s = ""
a += "|"
b += "|"

for _ in range(len(a) + len(b) - 2):
    if a < b:
        s = s + a[0]
        a = a[1:]
    else:
        s = s + b[0]
        b = b[1:]
print(s)
