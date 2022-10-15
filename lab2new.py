file_name=input("enter filename")
try:
    with open(file_name,'r') as f:
        print("The contents of the file is sorted order:")
        l=[]
        l=f.readlines()
        l.sort()
        print(l)
except FileNotFoundError as e:
    print("file doesn't exists")
    
            
    
