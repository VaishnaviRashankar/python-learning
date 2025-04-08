#polymorphism with classes method overriding
class Bird():
    def sound(self):
        print('Birds make sound')

class Crow(Bird):
    def sound(self):
        print("Crows say'Caw Caw'")
    
class Parrot(Bird):
    def sound(self):
        print('PArrot sound,squawk')
        
        
Bird1 = Crow()
Bird2 = Parrot()

Bird1.sound()
Bird2.sound()