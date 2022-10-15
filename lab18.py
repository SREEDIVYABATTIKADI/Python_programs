class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
class Stacksll:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False
    def push(self,ele):
            new_node=Node(ele)
            if self.isEmpty():
                self.top=new_node
            else:
                new_node.next=self.top
                self.top=new_node
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            temp=self.top
            self.top=self.top.next
            print(temp.data,"is deleted")
            del temp
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            temp=self.top
            print("the top element is:",self.top.data)
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("the elements are:")
            temp=self.top
            while temp!=None:
                print(temp.data)
                temp=temp.next
s=Stacksll()
n=int(input("enter element press -1 to stop"))
while n!=-1:
    s.push(n)
    n=int(input("enter element"))
s.display()
s.peek()
s.pop()
s.display()
