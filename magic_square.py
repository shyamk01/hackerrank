'''
Below code for all the combinations of magic numbers
m = [[a, b, c, d, e, f, g, h, i]
     for a in range(1, 10)
     for b in range(1, 10)
     for c in range(1, 10)
     for d in range(1, 10)
     for e in range(1, 10)
     for f in range(1, 10)
     for g in range(1, 10)
     for h in range(1, 10)
     for i in range(1, 10)
     if a+b+c==15 and d+e+f==15 and g+h+i==15 and a+d+g==15 and b+e+h==15 and c+f+i==15 and a+e+i==15 and c+e+g==15 and len(set([a,b,c,d,e,f,g,h,i]))==9
     ]'''

# https://www.hackerrank.com/challenges/magic-square-forming/problem
t = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
arr_t=[]
for a in t:
    arr_t+=a
x=[[2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
arr_min=set()
for a in x:
    sum=0
    for k in range(9):
       sum=sum+abs(a[k]-arr_t[k])
    arr_min.add(sum)

print(min(arr_min))