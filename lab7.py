def inp(sym):
    values={'+':1,'-':1,'*':3,'/':3,'^':6,'(':9,')':0}
    if sym in values.keys():
        return values[sym]
    else:
        return 7
def sp(sym):
    values={'+':2,'-':2,'*':4,'/':4,'^':5,'(':0,')':0}
    if sym in values.keys():
        return values[sym]
    else:
        return 8
class Stack:
    l=[]
    top=-1
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def push(self,ele):
        self.l.append(ele)
        self.top+=1
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            ele=self.l[self.top]
            self.l.pop()
            self.top-=1
            return ele
infix=input("enter infix expression by excluding brace at the begining and including $ at the end")#+")$"
postfix=""
s=Stack();
s.push('(')
for sym in infix:
    if sym=='$':
        break
    while inp(sym)<sp(s.l[s.top]):
        postfix=postfix+s.pop()
    if (inp(sym)>sp(s.l[s.top])):
        s.push(sym)
    else:
        s.pop()
print("The postfix expression is")
print(postfix)
