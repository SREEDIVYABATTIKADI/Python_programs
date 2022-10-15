r1=int(input("enter number of rows in matrix 1"))
c1=int(input("enter number of columns in matrix 1"))
r2=int(input("enter number of rows in matrix 2"))
c2=int(input("enter number of columns in matrix 2"))
if r1!=r2 or c1!=c2:
    print("addition of matrices cannot be done")
else:
    m1=[]
    m2=[]
    for i in range(r1):
        l=[]
        for j in range(c1):
            ele=int(input("enter elements into matrix 1"))
            l.append(ele)
        m1.append(l)
    for i in range(r2):
        l=[]
        for j in range(c2):
            ele=int(input("enter elements into matrix 2"))
            l.append(ele)
        m2.append(l)
    result=[]
    for i in range(r1):
        l=[]
        for j in range(c1):
            add=m1[i][j]+m2[i][j]
            l.append(add)
        result.append(l)
    print("The addition of two matrices :")
    for i in  range(r1):
        for j in range(c1):
            print(result[i][j],end=" ")
        print()
    




        
