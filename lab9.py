def rbinary(l,lb,ub,key):
    while lb<=ub:
        mid=(lb+ub)//2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            return rbinary(l,lb,mid-1,key)
        else:
            return rbinary(l,mid+1,ub,key)
    return -1
l=[]
n=int(input("enter n value:"))
for i in range(n):
    ele=int(input("enter element:"))
    l.append(ele)
print("elements before sorting are:",l)
l.sort()
print("elements after sorting are:",l)
key=int(input("enter key element:"))
loc=rbinary(l,0,n-1,key)
if loc==-1:
    print("search is not successful")
else:
    print("search is successful element found at location ",loc)
