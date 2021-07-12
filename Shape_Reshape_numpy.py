# https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy as np
x=input()
y =x.split(" ")
my_array=list(map(int,y))
print(np.reshape(my_array,(3,3)))
