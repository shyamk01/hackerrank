# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Beautiful Days at the Movies


i=20
j=23
k=6
cnt=0
for a in range(i,j+1):
    if((int(str(a)[::-1])-a)%k==0):
        cnt=cnt+1
print(cnt)