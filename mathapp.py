class app:
    
    def __init__(self,a,b):
        
        self.a=a
        self.b=b
        
        
    def sum(self):
        
        c=self.a+self.b
        
        return c
    def mul(self):
        
        c=self.a*self.b
        
        return c
    
    def  sub(self):
        
        c=self.a-self.b
        
        return c
    
    def   div(self):
        
        c=self.a/self.b
        return c
                
        
    


print("Enter the first number")
a=int(input())
print("Enter the second number")
b=int(input())

print ("1. sum \n2.MUL\n3.SUB\n4.div")

s1=app(a,b)

c=input("Enter the process you want to do")
c=int(c)


if c==1:
    
    r=s1.sum()
    print(" the result is ",r)
elif c==2:
    
    r=s1.mul()
    print(" the result is ",r)
elif  c==4:
    
    r=s1.div()
    print(" the result is ",r)

else:
    
    r=s1.sub()
    print("the result is ",r)

    

 