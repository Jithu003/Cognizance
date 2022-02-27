strng=input("Enter the string:")
x=len(strng)
evn=""
for i in range(0,x):
    if i%2==0:
        evn=evn+strng[i]
print(evn)
        
