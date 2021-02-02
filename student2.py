class student :
    
    
    
    def check_pass_fail(self):
        
        if self.marks>=40:
            return True
        
        else :
            return False
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
          

udent1=student("HArry",85)
student2=student("Rajib",35)
# print(udent1.name)
# print(udent1.marks)
# print(student2.name)
# print(student2.marks)

did_pass=udent1.check_pass_fail()

print(did_pass)

did_pass=student2.check_pass_fail()

print(did_pass)