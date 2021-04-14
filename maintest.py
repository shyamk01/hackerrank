arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
a = 0
n = 3
for i in range(n):
    a += arr[i][i]
    a -= arr[i][n-i-1]

print(abs(a))