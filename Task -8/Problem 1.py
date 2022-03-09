import numpy as np
a=np.array([10,11,12,13,14])
n=5
x=np.zeros(len(a)+(len(a)-1)*(n))
x[::n+1]=a
print(x)
