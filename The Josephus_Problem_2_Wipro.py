# The Josephus Problem - Numberphile
# Another solutions
def num(n):
    x= "{0:b}".format(n)
    y=x[1:len(x)]+x[0]
    return int(y, 2)

print(num(41))
