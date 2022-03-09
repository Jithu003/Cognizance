import numpy as np
a=[]
n=int(input("Size of first array:"))
for i in range(n):
    a.append(int(input("Element:")))
a=np.array(a)
print("First array:")
print(a)
b=[]
m=int(input("Size of second array:"))
for i in range(m):
    b.append(int(input("Element:")))
b=np.array(b)
print("Second array:")
print(b)
print("To check above mentioned array is equal or not")
x=np.allclose(a,b)
print(x)
 
