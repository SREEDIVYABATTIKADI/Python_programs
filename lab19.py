class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
class Queuell:
    def __init__(self):
        self.f=None
        self.r=None
    def isEmpty(self):
        if self.f==None and self.r==None:
            return True
        else:
            return False
    def enqueue(self,ele):
        new_node=Node(ele)
        if self.isEmpty():
            self.r=new_node
            self.f=new_node
        else:
            self.r.next=new_node
            self.r=new_node
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            temp=self.f
            self.f=self.f.next
            del temp
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print("the elements are:")
            temp=self.f
            while temp!=None:
                print(temp.data)
                temp=temp.next
q=Queuell()
n=int(input("enter element press -1 to stop"))
while n!=-1:
    q.enqueue(n)
    n=int(input("enter element"))
q.display()
print("after deleting an element from the from the front end of the queue")
q.dequeue()
q.display()
    
    
            
            
            
