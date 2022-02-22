f1=open("records.txt","w")
l1="Roll No"+ " "+"Name"+" "+"Marks"+"\n"
f1.write(l1)
f1.close()
f=open("records.txt","a")
n=int(input("Number of students:"))
for i in range(n):
    roll=int(input("Enter Students roll number:"))
    name=input("Enter students name:")
    marks=int(input("Enter students marks:"))
    l=str(roll)+"       "+name+"   "+str(marks)+"\n"
    f.write(l)
f.close()

#Subtask 1
f=open("records.txt","r")
c=f.read()
print(c)
f.close()

#Subtask 2
f=open("records.txt","r")
c=f.readlines()
print("The second record is:",c[2])
f.close()
    
