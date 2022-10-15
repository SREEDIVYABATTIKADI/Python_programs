file_name=input("enter file name")
try:
    with open(file_name,'r') as f:
        lines,words,characters=0,0,0
        for line in f:
            lines=lines+1
            words=words+len(line.split())
            characters=characters+len(line)
        print("No. of lines=",lines)
        print("No. of words=",words)
        print("No. of characters:",characters)
except FileNotFoundError as e:
    print("file does not exist")
    
