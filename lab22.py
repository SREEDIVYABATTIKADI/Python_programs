import sys
try:
    file1=sys.argv[1]
    file2=sys.argv[2]
    with open(file1,'r',) as f1 ,open(file2,'w') as f2:
        p=f1.read()
        f2.write(p)
        print("file copied successfully")
except FileNotFoundError as e:
    print("file doesnot exist",e)
except IndexError as e:
    print("provide arguments properly",e)
    
