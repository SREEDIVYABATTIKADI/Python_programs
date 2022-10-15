class Stackl:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l)==0:
            return True
        else:
            return False
    def push(self,ele):
        self.l.append(ele)
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            self.l.pop()
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.l[-1]
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("The elements are",self.l)
s=Stackl()
l=[]
n=int(input("Enter element press -1 to stop\n"))
while n!=-1:
    s.push(n)
    n=int(input("Enter element"))
s.display()
print("The last element is:",s.peek())
s.pop()
print("After deleting last element:")
s.display()
      
        
    
    
