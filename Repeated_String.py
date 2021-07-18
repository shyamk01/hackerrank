x = "a"
n = 1000000000000

z = len(x)
t = n // z
t1 = n % z

intt = x.count("a")
cnt = intt * t

cnt += x[0:t1].count("a")
print(cnt)
