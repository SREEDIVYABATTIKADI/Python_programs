list=[]
n=int(input("enter n value:"))
for i in range(n):
    l=[]
    name=input("enter name:")
    l.append(name)
    age=int(input("enter age:"))
    l.append(age)
    list.append(l);
print("before sorting",list)
print("after sorting")
print(sorted(list,key=lambda x:x[1]))

