file_name=input("enter filename")
try:
    with open(file_name,'r') as f:
        print("The contents of the file is sorted order:")
        l=[]
        for line in f:
            l.append(line)
        l.sort()
        print(l)
except FileNotFoundError as e:
    print("file doesn't exists")
    
            
    
