# https://www.hackerrank.com/challenges/maximize-it/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
'''
from itertools import product

inp_num = input()
n=int(inp_num.split(" ")[0])
mod=int(inp_num.split(" ")[1])
ats_max=set()
for _ in range(n):
    s=input()
    results = list(map(int, s.split(" ")))
    ax_max= map(lambda x:x**2%mod,results[1:len(results)])
    ats_max.add(ax_max)


print(max(map(lambda x: sum(x)%mod, product(*ats_max))))
