n = 15
c = 3
m = 2

choc = n // c
wrap = n // c

count = wrap
while wrap >= m:
    wrap = wrap - m
    count = count + 1
    wrap = wrap + 1

print(count)
