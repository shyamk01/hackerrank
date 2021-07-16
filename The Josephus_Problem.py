# The Josephus Problem - Numberphile
def num(n):
    n = 41
    x = 0
    l = 1
    while (n >= x):
        x = pow(2, l)
        l = l + 1

    l = l - 2
    l = n - pow(2, l)
    return 2 * l + 1
print(num(41))
