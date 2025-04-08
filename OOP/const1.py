class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age =age
        self.grade =grade

student1 = student('vaishnavi',100,'A+')
student2 = student('Vaish',90,'B+')

print(student1.name,student1.age,student1.grade)
print(student2.name,student2.age,student2.grade)

"""  
Type of constructor
 1 - default(self)
 2 - parameterize(self,name,age)
 3 - constructor with default values,(self,name = "unknown",age=0)
"""