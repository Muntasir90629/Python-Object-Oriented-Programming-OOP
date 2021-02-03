
class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
    
    class Laptop:
        
        def __init__(self):
            self.brand='HP'
            self.cpu="i5"
            self.ram=5
    
    
s1=Student("navin",2)
s2=Student("sabi",3)

print(s1.name,s1.rollno)   

print(s2.name,s2.rollno) 

lap1=s1.lap
lap2=s1.lap
print(id(lap1))
print(id(lap1))