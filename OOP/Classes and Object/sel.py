class student:
    def set_details(self,name,age):
        self.name = name
        self.age = age
        
student1 = student()
student1.set_details('vaishnavi',8)
print(student1.name,student1.age)