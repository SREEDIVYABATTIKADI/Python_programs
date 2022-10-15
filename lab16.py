class Node:
    def __init__(self,data):
        self.info=data
        self.next=None
class Dequeuesll:
    def __init__(self):
        self.f=None
        self.r=None
    def isEmpty(self):
        if self.f==None and self.r==None:
            return True
        else:
            return False
    def enqfirst(self,data):
        new_node=Node(data)
        if self.isEmpty():
            self.f=new_node
            self.r=new_node
        else:
            new_node.next=self.f
            self.f=new_node
    def enqlast(self,data):
        new_node=Node(data)
        if self.isEmpty():
            self.f=new_node
            self.r=new_node
        else:
            self.r.next=new_node
            self.r=new_node
    def deqfirst(self):
        if self.isEmpty():
            print("queue is empty")
        elif self.f==self.r:
            temp=self.f
            print(temp.info,"is deleted")
            del temp
            self.f=None
            self.r=None
        else:
            temp=self.f
            self.f=self.f.next
            print(temp.info,"is deleted")
            del temp
    def deqlast(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            temp=self.f
            if self.f==self.r:
                print(temp.info,"is deleted")
                del temp
            else:
                while temp.next!=None:
                    temp1=temp
                    temp=temp.next
                print(temp.info,"is deleted")
                self.r=temp1
                self.r.next=None
                del temp
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print("The elements are:")
            temp=self.f
            while temp!=None:
                print(temp.info)
                temp=temp.next
dq=Dequeuesll()
n=int(input("enter element press -1 to stop"))
while n!=-1:
    dq.enqlast(n)
    n=int(input("enter element"))
dq.display()
m=int(input("enter element at the last"))
dq.enqlast(m)
dq.display()
dq.deqlast()     
print("after deleting last element")
dq.display()
dq.deqfirst()
print("after deleting the first element")
dq.display()
    
    
        
                    
                    
                    
            
