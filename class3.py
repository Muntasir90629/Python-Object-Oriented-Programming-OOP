class Person:
    
    def __init__(self,name,age,add):
        
        
        self.name=name
        self.age=age
        self.add=add
   
    def myfunc(abc):
        
        print("your Name is ",abc.name)
        print("your age ",abc.age)
        
        print("your address",abc.add)
        
        
p1=Person("asif",20,"kotowali")

p1.myfunc()

