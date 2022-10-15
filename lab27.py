file_name=input("enter the file name")
try:
    with open(file_name,'r') as f:
        data=f.readlines()
        print(data)
    list=[]
    for line in data:
        word=line.split()
        list.extend(word)
    print(list)
    com=[]
    for word in list:
        if word not in com:
            com.append(word)
    print(word)
    for word in com:
        print(word,"appers in file",list.count(word))
except FileNotFoundError as e:
    print("file does not exists",e)
            
