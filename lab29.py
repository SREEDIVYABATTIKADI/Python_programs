import sys
try:
    file_name=sys.argv[1]
    n=int(sys.argv[2])
    with open(file_name,'r')as f:
        f.seek(n)
        print(f.read())
except FileNotFoundError as e:
    print("file doesnot exists",e)
except IndexError as e:
    print("provide proper number of arguments",e)
