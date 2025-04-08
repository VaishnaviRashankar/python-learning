class Animal:
    def speak(self):
        print('Animal make sounds')
class Dog(Animal):
    def bark(self):
         print('Dog Bark')
         
         
dog =Dog()
dog.speak()
dog.bark()

# if you create new method in child than it will override the exiting method