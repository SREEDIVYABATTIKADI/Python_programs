def insort(l,n):
    for i in range(1,n):
        t=l[i]
        j=i-1
        while j>=0 and t<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=t
l=[]
n=int(input("enter n value:"))
for i in range(n):
    ele=int(input("enter element"))
    l.append(ele)
print("before sorting elements are:",l)
insort(l,n)
print("after sorting elements are:",l)
    
