class Dequelist:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l)==0:
            return True
        else:
            return False
    def enqfirst(self,ele):
        self.l.insert(0,ele)
    def enqlast(self,ele):
        self.l.append(ele)
    def deqfirst(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.l.pop(0)
    def deqlast(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.l.pop()
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print("The elements are:",self.l)
dq=Dequelist()
l=[]
n=int(input("Enter element press -1 to stop"))
while n!=-1:
    dq.enqlast(n)
    n=int(input("Enter element"))
dq.display()
m=int(input("enter element at first"))
dq.enqfirst(m)
dq.display()
dq.deqfirst()
print("after deleting  first element")
dq.display()
dq.deqlast()
print("after deletinng last element")
dq.display()
