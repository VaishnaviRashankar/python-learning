"""  
constructor is a special methos which is called automatically when object called
 
 
__init__()
"""
# without constructor for understanding
class car:
    def set_details(self,brand,color):
        self.brand = brand
        self.color =color

car1 = car()
car1.set_details('BMW','Red')

print(car1.brand)
print(car1.color)