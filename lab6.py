class Complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im
    def __add__(self,other):
        return Complex(self.re+other.re,self.im+other.im)
    def __sub__(self,other):
        return Complex(self.re-other.re,self.im-other.im)
    def __mul__(self,other):
        real=(self.re*other.re)-(self.im*other.im)
        imaginary=(self.im*other.re)+(self.re*other.im)
        return Complex(real,imaginary)
    def display(self):
        print(self.re,"+(",self.im,")i")
r1=float(input("enter the real value of first complex number"))
i1=float(input("enter the imaginary value of first complex number"))
r2=float(input("enter the real value of second complex number"))
i2=float(input("enter the imaginary value of second complex number"))
c1=Complex(r1,i1)
c2=Complex(r2,i2)
print("addition of complex numbers:")
c3=c1+c2
c3.display()
print("subtraction of complex numbers:")
c3=c1-c2
c3.display()
print("multiplication of complex numbers:")
c3=c1*c2
c3.display()
