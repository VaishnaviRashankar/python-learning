from abc import ABC , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #no implementation
    
class Car(vehicle):
    def start(self):
        print('Car starts with a button')
        
        
class Bike(vehicle):
    def start(self):
        print('Bike starts with a button')
        
        
car = Car()
bike = Bike()

car.start()
bike.start()

# abstraction hide the uneccessary information from enduser make the structure easy
# abstract class can not be instantiate it act as a blue print
# child class must define abstarct classes
    