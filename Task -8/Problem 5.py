#Identity Matrix

import numpy as np
n=int(input("Enter number of Rows/Columns"))
print(np.identity(n))

#Multiplying A Matrix
a=np.array([[1,4,7],[2,5,8]])
b=np.array([[1,4],[2,5],[3,6]])
c=np.dot(a,b)
print(c)
