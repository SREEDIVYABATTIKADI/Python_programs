class Queue:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l)==0:
            return True
        else:
            return False
    def enqueue(self,ele):
        self.l.append(ele)
    def dequeue (self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.l.pop(0)
    def front(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            return self.l[0]#returning first entered element
    def rear(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            return self.l[-1]#returning the last entered element
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print("The elements in the queue are:",self.l)
q=Queue()
l=[]
n=int(input("enter elements press -1 to stop"))
while n!=-1:
    q.enqueue(n)
    n=int(input("enter element"))
q.display()
print("The last element in queue is ",q.rear())
print("the first element in queue is ",q.front())
print("after deleting the element in queue")
q.dequeue()
q.display()
        
    
        
