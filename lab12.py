def bsort(l,n):
    for p in range(n-1):
        for i in range(n-1):
            if l[i]>l[i+1]:
                t=l[i]
                l[i]=l[i+1]
                l[i+1]=t
l=[]
n=int(input("enter n value:"))
for i in range(n):
    ele=(input("enter element:"))
    l.append(ele)
print("before sorting:",l)
bsort(l,n)
print("after sorting:",l)
            
