class Stack:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l)==0:
            return True
        else:
            return False
    def push(self,ele):
        self.l.append(ele)
    def display(self):
        if self.isEmpty():
            print("list is empty")
        else:
            for i in self.l[::-1]:
                print(i,end=" ")
s=Stack()
n=int(input("enter the no of characters in your string"))
for i in range(n):
      ele=input("enter a string")
      s.push(ele)
s.display()
      
      
        
    
