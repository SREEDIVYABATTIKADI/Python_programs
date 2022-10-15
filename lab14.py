class Node:
    def __init__(self,data):
        self.info=data
        self.next=None
class Singlell:
    def __init__(self):
        self.head=None
    def create(self):
            data=int(input("enter data ,enter -1 to stop"))
            while data!=-1:
                new_node=Node(data)
                if self.head==None:
                    self.head=new_node
                    temp=self.head
                else:
                    temp.next=new_node
                    temp=new_node
                data=int(input("Enter data"))
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.info)
                temp=temp.next
    def delete(self):
        if self.head==None:
            print("list is empty")
        n=int(input("press 1 to delete at the begininng, 2 at the end,3 at a specific position"))
        if n==1:
            temp=self.head
            self.head=self.head.next
            del temp
        elif n==2:
            temp=self.head
            while temp.next!=None:
                temp1=temp
                temp=temp.next
            temp1.next=None
            del temp
        elif n==3:
            pos=int(input("enter position"))
            temp=self.head
            for i in range(pos-1):
                temp1=temp
                temp=temp.next
            temp1.next=temp.next
            del temp
        else:
            print("choose correct option")
sll=Singlell()
sll.create()
sll.display()
sll.delete()
sll.display()
            
        
                    
                    
                    
                
            
            
            
            
            

        
