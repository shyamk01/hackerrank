# https://www.hackerrank.com/challenges/strange-advertising/problem
# Viral Advertising


from math import floor

npbegin=5
npshare=3
nday=3
arr=[5]
npliked=floor(arr[0]/2)
for x1 in range(1,nday):
    arr.append(floor(arr[x1-1]/2)*3)
    npliked=npliked+floor(arr[x1]/2)

print(npliked)


