n=int(input("enter n value "))
print("The prime numbers up to the given number are")
for i in range(2,n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    
            
