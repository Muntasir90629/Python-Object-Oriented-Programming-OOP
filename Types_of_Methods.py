
class students:
    
    school="Teluska"
    
    def __init__(self,m1,m2,m3):
        
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def get_sch(cls):
        
        return cls.school
    @staticmethod
    def info():
        
        print("this is student class")
        
    
    # def get_m1(self):
    #     return self.m1
    
    # def set_m1(self,value):
    #     self.m1=value
         
    
        
s1=students(34,65,78)
s2=students(78,28,65)

print(s1.avg())
print(s2.avg())
print(students.get_sch())
students.info()