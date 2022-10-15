def ssort(l,n):
    for i in range(n-1):
        mi=i
        me=l[mi]
        for j in range(i+1,n):
            if l[j]<me:
                me=l[j]
                mi=j
        if mi!=i:
            t=l[mi]
            l[mi]=l[i]
            l[i]=t
l=[]
n=int(input("enter n a value:"))
for i in range(n):
    ele=int(input("enter element:"))
    l.append(ele)
print("before sorting:",l)
ssort(l,n)
print("after sorting:",l)
            
