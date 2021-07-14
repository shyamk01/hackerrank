import numpy

t=numpy.array([input().split() for _ in range(int(input()))],float)
print(round(numpy.linalg.det(t),2))