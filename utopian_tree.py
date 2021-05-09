n = 4
arr = [1]
for a in range(1, n + 1):
    if a % 2 == 0:
        arr.append(arr[a - 1] + 1)
    else:
        arr.append(arr[a - 1] * 2)

print(max(arr))
