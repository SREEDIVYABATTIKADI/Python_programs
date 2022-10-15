file_name=input("enter filename:")
s=input("enter string:")
try:
    with open(file_name,'r') as f:
        for line in f:
            if s in line:
                print(line)
        print("No such string exists")
except FileNotFoundError as e:
    print("file doesnot exists",)
