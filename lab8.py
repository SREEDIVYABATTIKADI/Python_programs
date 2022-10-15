def isOperator(i):
    oper=['+','-','*','/','^']
    if i in oper:
        return True
    else:
        return False
def Evaluation(a,b,i):
    if i=='+':
        return a+b
    elif i=='-':
        return a-b
    elif i=='*':
        return a*b
    elif i=='/':
        return a/b
    elif i=='^':
        return b**a
    else:
        print("invalid operator")
postfix=input("enter a postfix expression")
t=[]
for i in postfix:
    if isOperator(i):
        a=int(t.pop())
        b=int(t.pop())
        res=Evaluation(a,b,i)
        t.append(res)
    else:
        t.append(i)
print("the result is")
print(t[0])
        
