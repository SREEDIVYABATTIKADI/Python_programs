class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def displ(self):
        return self.l
    def dispb(self):
        return self.b
    def area(self):
        print("area=",self.l*self.b)
    def peri(self):
        print("perimeter=",2*(self.l+self.b))
    def isSquare(self):
        if(self.l==self.b):
            return True
        else:
            return False
l=int(input("enter length:"))
b=int(input("enter breadth:"))
r=Rectangle(l,b)
print("length is:",r.displ())
print("breadth is:",r.dispb())
r.area()
r.peri()
print("Is it a square:",r.isSquare())
    
        
